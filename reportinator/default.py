import sys
import reportinator.md2tex as md2tex

def main(section):
    return (md2tex.convert(section))


if __name__ == "__main__":
    section = sys.argv[1]
    print(main(section))
