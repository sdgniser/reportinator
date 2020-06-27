import os
import sys
from configurator import Config

cdir = str(os.path.dirname(os.path.realpath(sys.argv[0])))

config = Config(
    {
        "user": {
            "name": "unsetname",
            "affiliation": "unsetaffiliation",
            "style": "double",
        },
        "reconfig": True,
        "compiler": "none",
        "script": {
            "location": cdir,
            "locations": {
                "~/.reportinator/scripts",
                "~/.config/reportinator/scripts",
                "~/AppData/Local/Programs/reportinator/scripts",
            },
        },
        "layout": {
            "location": cdir,
            "locations": {
                "~/.reportinator/layouts",
                "~/.config/reportinator/layouts",
                "~/AppData/Local/Programs/reportinator/layouts",
            },
        },
        "locations": {
            "/etc/reportinator.yaml",
            "~/.reportinator/config.yaml",
            "~/.config/reportinator/config.yaml",
            "~/AppData/Local/Programs/reportinator/config.yaml",
        },
        "location": "",
    }
)

for dirs in config.locations:
    config = config + Config.from_path(dirs, optional=True)

for dirs in config.script.locations:
    dirs = os.path.expanduser(dirs)
    if os.path.isdir(dirs):
        config.script.location = dirs
        break

for dirs in config.locations:
    dirs = os.path.expanduser(dirs)
    if os.path.exists(dirs):
        config.location = dirs
        break

for dirs in config.layout.locations:
    dirs = os.path.expanduser(dirs)
    if os.path.isdir(dirs):
        config.layout.location = dirs
        break
