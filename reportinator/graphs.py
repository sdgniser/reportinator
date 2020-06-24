import argparse
import sys
import os
import csv
import reportinator
import reportinator.figures as figures


def main(section):
    output = ""
    output += "\n\\section{Graphs}\n"
    source_csv = []

    for file in os.listdir(reportinator.cache + "/csvs"):
        source_csv.append(file)

    def extract(string, start="(", stop=")"):
        try:
            return string[string.index(start) + 1: string.index(stop)]
        except:
            return None

    for source in source_csv:
        if source == ".DS_Store":
            continue
        csv_path = reportinator.cache + "/csvs/" + source
        data = list(csv.reader(open(csv_path)))
        lastline = data[-1]

        graphmatch = "\n".join(s for s in lastline if "graph(" in s).split("\n", 1)

        fitmatch = "\n".join(s for s in lastline if "fit(" in s).split("\n", 1)

        for graphs in graphmatch:
            foundfit = False
            if extract(fitmatch[0]) is not None:
                fit_list = extract(fitmatch[0])
                fitfun = fit_list
                fitmatch.pop(0)
                foundfit = True

            if extract(graphs) == None:
                print("WARNING: " + source + " is not being graphed")
                continue
            else:
                graph_list = extract(graphs).split(",")
            graph_list = (
                str(graph_list)
                .replace("[", "")
                .replace("]", "")
                .replace("'", "")
                .replace(" ", "")
            )
            n = str(source[:-4] + str(graphmatch.index(graphs)))
            if foundfit:
                output += figures.main(source, graph_list, n, fit=fitfun)
            else:
                output += figures.main(source, graph_list, n)
    return output


if __name__ == "__main__":
    section = sys.argv[1]
    print(main(section))
