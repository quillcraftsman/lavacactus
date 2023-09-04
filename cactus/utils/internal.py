#coding:utf-8
import contextlib
import six
import inspect

# Adapted from: http://kbyanc.blogspot.com/2007/07/python-more-generic-getargspec.html

FUNC_OBJ_ATTR = "__func__" if six.PY3 else "im_func"

# The alternate for inspect.ArgSpec which was deprecated
class ArgumentInfo:
    def __init__(self, args, varargs, varkw, defaults):
        self.args = args
        self.varargs = varargs
        self.varkw = varkw
        self.defaults = defaults

# format the spec to required format of ArgumentInfo
def get_argument_info(spec):
    spec_values = spec.parameters.values()
    args = []
    defaults = []

    for param in spec_values:
        args.append(param.name)
        if param.default != inspect.Parameter.empty:
            defaults.append(param.default)

    varargs = None
    varkw = None

    return ArgumentInfo(args, varargs, varkw, defaults)


# To remove the first parameter 'self' from object's spec
def remove_first_parameter(obj):
    # For methods or classmethods, drop the first
    # argument from the returned list because
    # Python supplies that automatically for us.
    # Note that this differs from what
    # inspect.getargspec() returns for methods.
    # NB: We use im_func so we work with
    #     instancemethod objects also.
    # Get the original signature
    original_spec = inspect.signature(getattr(obj, FUNC_OBJ_ATTR))
    # Get the parameters of the original signature
    original_parameters = list(original_spec.parameters.values())
    # Remove the first parameter (assuming it's the first one)
    new_parameters = original_parameters[1:]
    # Create a new signature with the updated parameters
    spec = original_spec.replace(parameters=new_parameters)
    return get_argument_info(spec)

def getargspec(obj):
    """
    Get the names and default values of a callable's
       arguments

    A tuple of four things is returned: (args, varargs,
    varkw, defaults).
      - args is a list of the argument names (it may
        contain nested lists).
      - varargs and varkw are the names of the * and
        ** arguments or None.
      - defaults is a tuple of default argument values
        or None if there are no default arguments; if
        this tuple has n elements, they correspond to
        the last n elements listed in args.

    Unlike inspect.getargspec(), can return argument
    specification for functions, methods, callable
    objects, and classes.  Does not support builtin
    functions or methods.
    """
    if not callable(obj):
        raise TypeError(f"{type(obj)} is not callable")

    with contextlib.suppress(NotImplementedError):
        if inspect.isfunction(obj):
            spec = inspect.signature(obj)
            return get_argument_info(spec)

        elif hasattr(obj, FUNC_OBJ_ATTR):
            return remove_first_parameter(obj)
        elif inspect.isclass(obj):
            return getargspec(obj.__init__)

        elif isinstance(obj, object):
            # We already know the instance is callable,
            # so it must have a __call__ method defined.
            # Return the arguments it expects.
            return getargspec(obj.__call__)

    raise NotImplementedError(f"do not know how to get argument list for {type(obj)}")
