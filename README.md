# Aim of the Project:
To make LaTeX reports easily from markdowns, containing the section data, autoplotted graphs from CSV, . Please look at the example first, before doing anything. Please install [Typora](https://typora.io), a MarkDown reader (not necessary, but recommended) and the latest version of [Python](https://python.org/downloads). 

## Installation:
Please ensure that you have atleast Python3.6+
Clone the repo:
```shell
git clone "https://github.com/sdgniser/reportinator"
```
or by just downloading and unzipping this in your own location.
To build this package with pip, just:
```shell
python -m pip install -e path/to/the/clone/directory/
```
For windows, `py` may replace `python`.
**NOTE** for Windows Users: You would have to logout and login once the program is installed. This will make sure that the `PATH` added is implemented. You might even want to use a more user-friendly interface. A python script gets made in the Desktop, which is named `make-my-report.py`. You can copy this script to your project directory, and just run it with python by using the terminal or by right clicking and then selecting open with python.

A thing to note here is that on first installation, reportinator will exit after collecting metadata. So you will need to run it again.

## Dependencies:
You do not need to install these, pip does that by itself. But heres a list of what gets installed. We are not listing the things the dependencies install.
* matplotlib
* numpy
* ruamel.yaml
* doi2bib
* pandas
* pyyaml
* configurator

## Basic Usage:
This needs python3.6+, nothing below is supported. After the pip installation, you can easily call this from anywhere using the terminal/powershell. Just go to the directory where you have the markdown files/source csv files and the images and:
```shell
reportinator
```
This should run configuration once its started for the first time. If at any point you want to reconfigure:
```shell
reportinator --reconfig
```
If you want to have your own script bring run in one of the sections, say you want some custom code to output something in `Example` section, you need to make an `Example.py` and run:
```shell
reportinator --install Example.py
```
You can tweak the scripts in the program in the clone directory or just run say, 
```shell
reportinator --install Default.py
```
to replace the `Default.py` usage in the code. However for making your own scripts, you need to follow the format as shown in `example/Template.py`. A working example named `example/Example.py` has been placed for further reference.
If you want to run this code from somewhere else, you can always do:
```shell
reportinator --source path/to/project/directory
```
If you are stuck, do:
```shell
reportinator --help
```

## Input Markdown:
The name of the input markdown is the title of the report. Recommended use: Typora, as a markdown editor, otherwise:

For recognizing multiple subsections, or lists with a text above them, it is necessary that you leave a one line gap between each subsection, or before the list. There is an example loaded in the current repo, which may be referred to, initially.
**Tables and Graphs will only be plotted only if the program sees the appropriate section headings.** If you are leaving some section like graphs blank, and want to only fill it up with python graphs, you need to leave one blank line in the section. That is, you must have atleast one line in each section, even if it is blank.

### Equations:
For putting in equations, you must type:
```markdown
$$ your-equation $$ #e:tag
```
For referencing them anywhere inside the text, you just need to type `@e:tag` at the appropriate place.

### Images:
Just use the default markdown syntax for images. You can drag and drop images in typora. No need to type.
```markdown
![This is the caption](image.png)
```
Refer to these images by saying @f:name in-text.

### Tables:
All the csv files placed in the source folder will be converted to tables. For good looking reports, please make sure that there are a maximum of 4 columns, in double column. To refer to the table anywhere, you do `@t:csvname`. You can use excel too. Just keep the .xlsx in your project directory and have the names of the sheets, what you would want the caption of the table.

### Graphs:
These are triggered by a graph statement at the end of the csvfile (Look at the example in example). So if the line contains `graph(x,y)`, then a graph will be plotted. Writing `fit(lin)` next will fit the graph in the said format. Look at the example.
You can fit polynomial functions till 4 order. To refer to a graph, you need to do `@g:graphname`. The graph name is y column name without \ and $ and the order number. So, it might be `Potential1`.

### Referencing:
You can add references by just adding a dois.txt file, containing the list of dois in your source directory. You might need to manually compile it to actually get the references printed. Please note that you can just not use the referencing schemes explained above with the `@` and just type `\ref{something}` to use the default syntax.

### Compiling:
Autocompile is toggled on if there is a compiler installation in the system.

## Templates
This code supports templates. All the class files are to be stored in `_layouts/`. Please add these lines to your custom class file, after `\NeedsTeXFormat{LaTeX2e}`:
```latex
 \usepackage[utf8]{inputenc}
 \usepackage{times}
 \usepackage{graphicx}
 \usepackage{amssymb}
 \usepackage{textcomp}
 \usepackage{gensymb}
 \usepackage{amsmath}
 \usepackage{float}
 \usepackage{booktabs}
 \usepackage[table,xcdraw]{xcolor}
 \providecommand{\tightlist}{%
   \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
```
The graph python code uses seaborn, you may look at the different styles available in the internet for the same, and change it in `share/figures.py`

# To do:
* PyPi submission
* Tightlist integration
* _Proper fitting in the graph (more functions)_
* _Error analysis code_
* _Auto break for equations_
* _Consistent font size and column width in tables_

# Example:
One example has been given in the program at `example`

# The Maintainers:
This project is being maintained by Spandan Anupam and Visnhu Namboodiri K S. Thank us by using this program.
