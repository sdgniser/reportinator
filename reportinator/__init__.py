from .config import config
import os
import tempfile

__all__ = (
    "scriptmatcher",
    "config",
    "default",
    "graphs",
    "figures",
    "header",
    "observations",
    "md2tex",
    "references",
    "functions",
    "main",
    "win_add2path",
    "reconfig",
    "abstract",
    "footer",
)

tempfile.tempdir = tempfile.gettempdir() + "/reportinator"
cache = tempfile.gettempdir()
