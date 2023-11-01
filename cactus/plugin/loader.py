#coding:utf-8
import importlib
import os
import sys
import logging
import types
# from imp import load_source
from importlib.machinery import SourceFileLoader
from importlib.util import spec_from_file_location, module_from_spec, spec_from_loader

from cactus.plugin import defaults
from cactus.utils.filesystem import fileList


logger = logging.getLogger(__name__)


def load_source_new(modname, filename):
    loader = importlib.machinery.SourceFileLoader(modname, filename)
    spec = importlib.util.spec_from_file_location(modname, filename, loader=loader)
    module = importlib.util.module_from_spec(spec)
    # The module is always executed and not cached in sys.modules.
    # Uncomment the following line to cache the module.
    sys.modules[module.__name__] = module
    loader.exec_module(module)
    return module


class BasePluginsLoader(object):
    def load(self):
        raise NotImplementedError("Subclasses must implement load")

    def _initialize_plugin(self, plugin):
        """
        :param plugin: A plugin to initialize.
        :returns: An initialized plugin with all default methods set.
        """
        # Load default attributes
        for attr in defaults.DEFAULTS + ['ORDER']:
            if not hasattr(plugin, attr):
                setattr(plugin, attr, getattr(defaults, attr))

        # Name the plugin
        if not hasattr(plugin, "plugin_name"):
            if hasattr(plugin, "__name__"):
                plugin.plugin_name = plugin.__name__
            elif hasattr(plugin, "__class__"):
                plugin.plugin_name = plugin.__class__.__name__
            else:
                plugin.plugin_name = "anonymous"


class ObjectsPluginLoader(BasePluginsLoader):
    """
    Loads the plugins objects passed to this loader.
    """
    def __init__(self, plugins):
        """
        :param plugins: The list of plugins this loader should load.
        """
        self.plugins = plugins

    def load(self):
        """
        :returns: The list of plugins loaded by this loader.
        """
        plugins = []

        # Load cactus internal plugins
        for builtin_plugin in self.plugins:
            self._initialize_plugin(builtin_plugin)
            plugins.append(builtin_plugin)

        return plugins


class CustomPluginsLoader(BasePluginsLoader):
    """
    Loads all the plugins found at the path passed.
    """

    def __init__(self, plugin_path):
        """
        :param plugin_path: The path where the plugins should be loaded from.
        """
        self.plugin_path = plugin_path

    def load(self):
        """
        :returns: The list of plugins loaded by this loader.
        """
        plugins = []

        # Load user plugins
        for plugin_path in fileList(self.plugin_path):
            if self._is_plugin_path(plugin_path):
                custom_plugin = self._load_plugin_path(plugin_path)
                if custom_plugin:
                    self._initialize_plugin(custom_plugin)
                    plugins.append(custom_plugin)


        return plugins

    def _is_plugin_path(self, plugin_path):
        """
        :param plugin_path: A path where to look for a plugin.
        :returns: Whether this path looks like an enabled plugin.
        """
        if not plugin_path.endswith('.py'):
            return False

        if 'disabled' in plugin_path:
            return False

        return True

    def _load_from_source(self, module_name, plugin_path):
        # # One way
        # loader = SourceFileLoader(module_name, plugin_path)
        # module = types.ModuleType(loader.name)
        # loader.exec_module(module)
        #
        # # Second way
        # loader = importlib.machinery.SourceFileLoader(module_name, plugin_path)
        # module = loader.load_module()
        #
        # # Third way
        # spec = importlib.util.spec_from_file_location(module_name, plugin_path)
        # module = importlib.util.module_from_spec(spec)
        # sys.modules[module_name] = module
        # spec.loader.exec_module(module)

        # Next way
        loader = importlib.machinery.SourceFileLoader(module_name, plugin_path)
        module = types.ModuleType(loader.name)
        module.__file__ = plugin_path
        sys.modules[module.__name__] = module
        loader.exec_module(module)

        # Old way
        # module = load_source(module_name, plugin_path)

        # Result
        return module

    def _load_plugin_path(self, plugin_path):
        """
        :param plugin_path: A path to load as a plugin.
        :returns: A plugin module.
        """
        module_name = "plugin_{0}".format(os.path.splitext(os.path.basename(plugin_path))[0])

        try:
            # module = self._load_from_source(module_name, plugin_path)
            module = load_source_new(module_name, plugin_path)
            return module
        except Exception as e:
            logger.warning('Could not load plugin at path %s: %s' % (plugin_path, e))
            return None

            # sys.exit()
