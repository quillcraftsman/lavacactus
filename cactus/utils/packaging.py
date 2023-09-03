import posixpath
import os

PATH = os.path.dirname(__file__).rstrip('utils')


def pkg_walk(top):
    # we get names tuple names where names[0] is current folder, names[1] is list of dirs and names[2] is list of files
    cur_dir, dirs, non_dirs = next(os.walk(os.path.join(PATH, top)))
    yield top, dirs, non_dirs
    # loop through dirs to do the same thing as we did before
    for name in dirs:
        new_path = posixpath.join(top, name)
        for out in pkg_walk(new_path):
            yield out
