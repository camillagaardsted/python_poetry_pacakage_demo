import sys

if sys.version_info >= (3, 8):
    from importlib import metadata
    __version__ = metadata.version('mypackage_demo')


