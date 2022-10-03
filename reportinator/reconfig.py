import os
import sys
import fileinput
import argparse
import shutil
import ruamel.yaml


def main(conf, *args, **kwargs):
    import os
    import sys
    import fileinput
    import argparse
    import shutil
    import ruamel.yaml

    if kwargs.get("first_install", None):
        import pkg_resources
        import os
        import shutil

        if os.path.exists(os.path.expanduser("~/Desktop")):
            if pkg_resources.resource_exists(
                "reportinator", "scripts/make-my-report.py"
            ):
                shutil.copy(
                    pkg_resources.resource_filename(
                        "reportinator", "scripts/make-my-report.py"
                    ),
                    os.path.expanduser("~/Desktop/make-my-report.py"),
                )
        try:
            import reportinator.win_add2path

            reportinator.win_add2path.main()
        except ModuleNotFoundError:
            pass
        sys.exit(0)

    yaml = ruamel.yaml.YAML()
    configlist = ["~/.config", "~/AppData/Local/Programs"]
    default_config = """
    user:
      name: unsetname
      affiliation: unsetaffiliation
      style: double

    reconfig: True
    compiler: none
    """

    for dirs in configlist:
        dirs = os.path.expanduser(dirs)
        if os.path.isdir(dirs):
            configpath = dirs + "/reportinator/config.yaml"
            try:
                os.makedirs(dirs + "/reportinator/layouts")
                os.makedirs(dirs + "/reportinator/scripts")
            except FileExistsError:
                pass

    if not os.path.exists(configpath):
        with open(configpath, "w") as f:
            f.write(default_config)

    print("Find your configuration file at: " + configpath)

    with open(configpath) as f:
        config = yaml.load(f)

    if not conf:
        name = input("Enter name: ")
        affiliation = input("Enter affiliation: ")
        style = input("Enter name of the custom class file (Leave blank for default): ")

        if name:
            config["user"]["name"] = name
        if affiliation:
            config["user"]["affiliation"] = affiliation
        if style:
            config["user"]["style"] = style
        else:
            config["user"]["style"] = "double"

        if shutil.which("latexmk"):
            config["compiler"] = "latexmk -pdf -bibtex -f -silent"
        elif shutil.which("pydflatex"):
            config["compiler"] = "pydflatex -t -k -o"
        elif shutil.which("pdflatex"):
            config[
                "compiler"
            ] = "pdflatex -interaction nonstopmode -halt-on-error -file-line-error"
        elif shutil.which("xelatex"):
            config["compiler"] = "xelatex"
        elif shutil.which("lualatex"):
            config["compiler"] = "lualatex"
        else:
            config["compiler"] = "none"

        config["reconfig"] = False

    with open(configpath, "w") as f:
        yaml.dump(config, f)


if __name__ == "__main__":
    conf = False
    main(conf)
