import posixpath
import pkg_resources
import os


def pkg_walk(package, top):
    """
    Walk the package resources. Implementation from os.walk.
    """
    names = pkg_resources.resource_listdir(package, top)
    dirs, nondirs = [], []

    for name in names:
        # Forward slashes with pkg_resources
        if pkg_resources.resource_isdir(package, posixpath.join(top, name)):
            dirs.append(name)
        else:
            nondirs.append(name)
    yield top, dirs, nondirs

    for name in dirs:
        new_path = posixpath.join(top, name)
        for out in pkg_walk(package, new_path):
            yield out


def pkg_walk_2(package, top):
    # we get names tuple names where names[0] is current folder, names[1] is list of dirs and names[2] is list of files
    names = os.walk(os.path.join(package, top)).__next__()
    dirs, nondirs = [dir for dir in names[1]], [nondir for nondir in names[2]]
    yield top, dirs, nondirs
    # loop through dirs to do the same thing as we did before
    for name in dirs:
        new_path = posixpath.join(top, name)
        for out in pkg_walk_2(package, new_path):
            yield out
