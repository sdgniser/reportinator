import os
import sys
import reportinator.config
import reportinator


def main(section):
    title = "title"

    for file in os.listdir(reportinator.cache):
        ext = os.path.splitext(file)[1]
        if ext == ".md":
            title = os.path.splitext(file)[0]

    header = """
\\documentclass{%s}
\\begin{document}
\\title{%s}
\\author{%s\\thanks{%s}}
\\date{\\today}
\\maketitle
    """ % (
        reportinator.config.user.style,
        title,
        reportinator.config.user.name,
        reportinator.config.user.affiliation,
    )
    return header


if __name__ == "__main__":
    section = sys.argv[1]
    print(main(section))
