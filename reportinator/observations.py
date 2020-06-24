import pandas
import io
import os
import sys
import reportinator

def main(section):
    output = ""
    output += "\n\\section{Observations}\n"
    cache_dir = reportinator.cache

    def convertToLaTeX(names, df, alignment="c"):
        numColumns = df.shape[1]
        numRows = df.shape[0]
        output = io.StringIO()
        colFormat = ("%s|" % (("|" + alignment) * numColumns))
        # Write header
        output.write("\\begin{table}[H]\n")
        output.write("\\centering")
        output.write("\\resizebox{\\columnwidth}{!}{")
        output.write("\\begin{tabular}{%s}\n" % colFormat)
        columnLabels = ["\\textbf{%s}" % label for label in df.columns]
        output.write("\\hline%s\\\\\\hline\n" % " & ".join(columnLabels))
        # Write data lines
        for i in range(numRows):
            output.write("%s\\\\\\hline\n"
                         % (" & ".join([str(val) for val in df.iloc[i]])))
        # Write footer
        output.write("\\end{tabular}}\n")
        output.write("\\caption{" + names + "}\n")
        output.write("\\label{t:" + names + "}")
        output.write("\\end{table}")
        return output.getvalue()

    # EXCEL
    if os.path.exists(cache_dir + "/data.xlsx"):
        path = cache_dir + "/data.xlsx"
        xls = pandas.ExcelFile(path)
        sheets = xls.sheet_names

        for sheet in sheets:
            names = str(sheet)
            df = pandas.read_excel(xls, sheet_name = sheet, index_col = None)
            df.fillna('', inplace = True)
            df = df.round(decimals = 2)
            with open(cache_dir + "/csvs/" + sheet + ".csv", 'w+') as csvfile:
                df.to_csv(csvfile, encoding = 'utf8', index = False)

    # CSV FILES
    if not os.listdir(cache_dir + "/csvs/"):
        pass
    else:
        for item in os.listdir(cache_dir + "/csvs/"):
            path = cache_dir+"/csvs/" + item
            df = pandas.read_csv(path)
            df = df.round(decimals = 2)
            df.fillna('', inplace = True)
            checkstr = str(df.iloc[-1:])
            if "graph" in checkstr:
                df.drop(df.tail(1).index,inplace = True)
            names = str(item[:-4])
            output += convertToLaTeX(names,df,alignment = 'c')


    return output

if __name__ == "__main__":
    section = sys.argv[1]
    print(main(section))
