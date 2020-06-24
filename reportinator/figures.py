# using seaborn as stylesheet
# https://python-graph-gallery.com/106-seaborn-style-on-matplotlib-plot/
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse
import sys
import os
import reportinator.functions as fn
import reportinator
import reportinator.config

from scipy.optimize import curve_fit


def main(file, lister, index, *args, **kwargs):
    if reportinator.config.compiler == "none":
        usetex = False
    else:
        usetex = True
    cache_dir = reportinator.cache
    plt.style.use("bmh")

    # parser
    fun = kwargs.get("fit", None)
    n = index
    y_name_list = []
    y_list = []
    in_file = cache_dir + "/csvs/" + file
    y_list = (lister).split(",")
    y_list = [int(x) - 1 for x in y_list]
    x_index = y_list.pop(0)
    data = pd.read_csv(in_file)
    data = data[:-1]
    x_name = data.columns[x_index]
    for y_index in y_list:
        y_name_list.append(data.columns[y_index])

    # actual plotting and saving in PDF
    def plot(x_name, y_name_list, data, n):
        x = data[x_name]
        x = list(map(float, x))
        f = plt.figure()
        plt.rc("text", usetex=usetex)
        plt.rc("font", family="serif")
        i = 0
        markers = ["o", "+", "s", "^", "x", "D", "v"]
        for y_name in y_name_list:
            y = data[y_name]
            y = list(map(float, y))
            plt.scatter(
                x,
                y,
                marker=markers[i],
                color="#FFA500",
                label="Observed, for " + y_name,
            )
            if not fun:
                cap = False
                pass
            else:
                p, _, cap = fit(x, y, fun)
                fitfig = np.poly1d(p)
                plt.plot(
                    x,
                    fitfig(x),
                    linestyle="dotted",
                    color="#000000",
                    label="Fitted Data",
                )
            i += 1
        plt.xlabel(r"%s" % x_name, fontsize=13)
        plt.ylabel(r"%s" % y_name, fontsize=13)
        plt.legend()
        if "$" in y_name:
            y_new = y_name.replace("$", "")
            y_new = y_new.replace("\\", "")
            f.savefig(
                cache_dir + "/" + y_new.split(" ")[0] + n + ".pdf", bbox_inches="tight"
            )
        else:
            f.savefig(
                cache_dir + "/" + y_name.split(" ")[0] + n + ".pdf", bbox_inches="tight"
            )
        return cap

    def pregraph(name, n, cap):
        output = ""
        if "$" in name:
            name = name.replace("$", "")
            name = name.replace("\\", "")
        location = "./" + name.split(" ")[0] + n + ".pdf"
        tag = name.split(" ")[0]
        tag_new = tag.lower()
        if not cap:
            output = (
                "\\begin{figure}[H]"
                + "\n"
                + "\\centering"
                + "\n"
                + "\\includegraphics[width = \\columnwidth]"
                + "{"
                + location
                + "}"
                + "\n"
                + "\\caption{"
                + tag
                + "}"
                + "\n"
                + '\\label{g:"'
                + tag_new
                + '"}'
                + "\n"
                + "\\end{figure}"
            )
        else:
            output = (
                "\\begin{figure}[H]"
                + "\n"
                + "\\centering"
                + "\n"
                + "\\includegraphics[width = \\columnwidth]"
                + "{"
                + location
                + "}"
                + "\n"
                + "\\caption{"
                + tag
                + ", "
                + cap
                + "}"
                + "\n"
                + '\\label{g:"'
                + tag_new
                + '"}'
                + "\n"
                + "\\end{figure}"
            )
        return output

    def fit(x, y, fun):
        output = ""
        if fun == "lin":
            p, pcov = curve_fit(fn.lin, x, y)
            p_sigma = np.sqrt(np.diag(pcov))

        elif fun == "quad":
            p, pcov = curve_fit(fn.quad, x, y)
            p_sigma = np.sqrt(np.diag(pcov))

        elif fun == "exp":
            p, pcov = curve_fit(fn.exp, x, y)
            p_sigma = np.sqrt(np.diag(pcov))

        elif fun == "log":
            p, pcov = curve_fit(fn.log, x, y)
            p_sigma = np.sqrt(np.diag(pcov))

        elif fun == "gauss":
            p, pcov = curve_fit(fn.gauss, x, y)
            p_sigma = np.sqrt(np.diag(pcov))

        elif fun == "boltz":
            p, pcov = curve_fit(fn.boltz, x, y)
            p_sigma = np.sqrt(np.diag(pcov))

        else:
            output += "Wrong function"

        cap = f"{fn.txt(fun, p, p_sigma)!s}"

        return p, pcov, cap

    cap = plot(x_name, y_name_list, data, n)
    return pregraph(y_name_list[-1], n, cap)


if __name__ == "__main__":
    file = ""
    lister = ""
    index = ""
    fitfun = "lin"
    print(main(file, lister, index, fit=fitfun))
