# coding:utf-8
import os
import posixpath  # TODO: Windows?
import logging
from cactus.utils.packaging import pkg_walk, PATH

logger = logging.getLogger(__name__)


def bootstrap_from_package(path):
    for dir_, sub_dirs, filenames in pkg_walk("skeleton"):
        base_path = os.path.join(path, dir_.split('skeleton', 1)[1].lstrip('/'))
        for sub_dir in sub_dirs:
            dir_path = os.path.join(base_path, sub_dir)
            logger.debug("Creating {0}".format(dir_path))
            os.makedirs(dir_path)

        for filename in filenames:
            resource_path = posixpath.join(dir_, filename)
            file_path = os.path.join(base_path, filename)

            logger.debug("Copying {0} to {1}".format(resource_path, file_path))
            with open(file_path, 'wb') as f_writer:
                with open(os.path.join(PATH, resource_path), "rb") as f_reader:
                    f_writer.write(f_reader.read())
