#!/usr/bin/env python3
import sys


def main():
    import os
    import glob
    import argparse
    import sys
    import shutil
    import reportinator
    from distutils.dir_util import copy_tree
    import reportinator.scriptmatcher
    import pkg_resources

    path = os.getcwd()
    shutil.rmtree(path + "/__pycache__", ignore_errors=True, onerror=None)
    config = reportinator.config

    if config.user.name == "unsetname":
        print("Performing reconfiguration setup...")
        import reportinator.reconfig

        reportinator.reconfig.main()
        print(
            "Reconfiguration complete. Run reportinator again to process your report."
        )
        exit()

    output = ""

    parser = argparse.ArgumentParser(description="Welcome to Reportinator 1.0")
    parser.add_argument(
        "--source",
        required=False,
        default=False,
        help="Directory path of the source files, without / at the end",
    )
    parser.add_argument(
        "--install",
        required=False,
        default=False,
        help="Directory path of the source files, without / at the end",
    )
    parser.add_argument(
        "--reconfig",
        required=False,
        default=False,
        action="store_true",
        help="Run the reconfiguration script",
    )
    args = parser.parse_args()

    if args.source:
        path = args.source

    if args.install:
        if os.path.exists(args.install):
            shutil.copy(args.install, config.script.location + "/" + args.install)
            print("New script installed: " + args.install)
        exit()

    if config.reconfig or args.reconfig:
        print("Performing reconfiguration setup...")
        import reportinator.reconfig

        reportinator.reconfig.main()
        print(
            "Reconfiguration complete. Run reportinator again to process your report."
        )
        exit()

    documentstyle = config.user.style
    cache_dir = reportinator.cache

    print("Your LaTeX code is being processed. Please check your source directory")

    # Copying over files to cache directory
    shutil.rmtree(cache_dir, ignore_errors=True, onerror=None)
    try:
        os.mkdir(cache_dir)
        os.mkdir(cache_dir + "/csvs")
    except:
        pass

    for file in os.listdir(path):
        ext = os.path.splitext(file)[1]
        if ext == ".md":
            tempath = cache_dir + "/" + file
            shutil.copy(path + "/" + file, cache_dir + "/" + file)
        elif ext == ".csv":
            shutil.copy(path + "/" + file, cache_dir + "/csvs/" + file)
        else:
            shutil.copy(path + "/" + file, cache_dir + "/" + file)
    try:
        os.remove(cache_dir + "/output.tex")
    except OSError:
        pass

    # Iterating Over Sections and Calling Scripts
    with open(tempath) as f:
        lines = f.readlines()

    sections = list()
    section = ""
    for line in lines:
        if line[:2] == "# ":
            sections.append(section)
            section = ""
        section += line
    sections.append(section)

    output += reportinator.scriptmatcher.main("Header", "")
    for section in sections[1:]:
        name = section.split("\n", 1)[0][2:]
        print("Processing " + name)
        output += reportinator.scriptmatcher.main(name, section)
    output += reportinator.scriptmatcher.main("Footer", "")

    with open(cache_dir + "/output.tex", "w") as f:
        f.write(output)

    # Copying files back
    copy_tree(cache_dir, path)

    if pkg_resources.resource_exists(
        "reportinator", "layouts/" + documentstyle + ".cls"
    ):
        shutil.copy(
            pkg_resources.resource_filename(
                "reportinator", "layouts/" + documentstyle + ".cls"
            ),
            path + "/" + documentstyle + ".cls",
        )

    shutil.rmtree(path + "/csvs", ignore_errors=True, onerror=None)

    # Compilation
    os.chdir(path)
    if config.compiler == "none":
        pass
    else:
        try:
            compiler = config.compiler
            os.system(compiler + " output.tex")
            os.system(compiler + " output.tex")

        except:
            print("Couldn't Compile LaTeX using " + compiler)
    if shutil.which("latexmk"):
        os.system("latexmk -c")
    for f in glob.iglob(
        "*.aux"
        or "*.bcf"
        or "*.log"
        or "*.run.xml"
        or "*.fls"
        or ".fbd.latexmk"
        or ".blg"
    ):
        os.remove(f)

    print("Your shit's sorted")


if __name__ == "__main__":
    main()
