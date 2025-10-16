from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("sysinfo-cli")
except PackageNotFoundError:
    __version__ = "0.0.0"
