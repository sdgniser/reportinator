#!/bin/python
import os
import sys
import reportinator
import reportinator.scriptmatcher
from doi2bib.crossref import get_bib_from_doi


def main(section):
    output = ""
    out = reportinator.cache + "/output.bib"
    inp = reportinator.cache + "/dois.txt"
    f = open(out, "w+")
    fp = open(inp, "r")
    for line in fp:
        doi = line.split(" ")[0]
        found, bib = get_bib_from_doi(doi)
        if found:
            f.write(bib + "\n")
    output += "\n\\section{References}\n"
    output += "\\nocite{" + "*}\n"
    output += "\\printbibliography[heading=none]\n\n"
    return output


if __name__ == "__main__":
    section = sys.argv[1]
    print(main(section))
