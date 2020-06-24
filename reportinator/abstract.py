import reportinator.config as config
import reportinator.md2tex
import sys


def main(section):
    section = "\n".join(section.split("\n")[1:])
    output = ""
    output += "\\begin{abstract}\n"
    output += reportinator.md2tex.convert(section) + "\n"
    output += "\\end{abstract}\n"
    return output


if __name__ == "__main__":
    section = sys.argv[1]
    print(main(section))
