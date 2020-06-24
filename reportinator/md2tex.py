import sys
import re
import os

def convert(string):
    string = '\n' + string

    # Images
    newstring=""
    for line in string.splitlines():
        if '![' in line:
            image_text = """
\\begin{figure}[H]
    \\includegraphics[width = \\columnwidth]{%s}
    \\centering
    \\caption{%s}
    \\label{%s}
\\end{figure}
            """ % (re.findall('!\\[.*\\]\\((.*)\\)', line)[0], re.findall('!\\[(.*)\\]', line)[0], 'f:' + re.findall('!\\[.*\\]\\((.*)\\)', line)[0].split('.')[0])
            newstring = newstring + image_text
            line = ""
        newstring = newstring + line + '\n'
    string = newstring


    # Section Headers
    string = re.sub(r'\n#### (.*)', r'\n\\subsubsubsection{\1}', string)
    string = re.sub(r'\n### (.*)', r'\n\\subsubsection{\1}', string)
    string = re.sub(r'\n## (.*)', r'\n\\subsection{\1}', string)
    string = re.sub(r'\n# (.*)', r'\n\\section{\1}', string)


    # Bold
    string = re.sub(r'__(.*)__', r'\\textbf{\1}', string)
    string = re.sub(r'\*\*(.*)\*\*', r'\\textbf{\1}', string)

    # Italics
    # string = re.sub(r'_(.*)_', r'\\textit{\1}', string)
    string = re.sub(r'\*(.*)\*', r'\\textit{\1}', string)

    # Math
    string = re.sub(r'\n *\$\$(.*)\$\$ *#(\S*:\S*)', r'\n\\begin{align}\n\t\1\n\t\\label{\2}\n\\end{align}\n', string)
    string= re.sub(r'\n *\$\$(.*)\$\$', r'\n\\begin{align}\n\1\n\\end{align}\n', string)


    # Unordered Lists
    string = re.sub(r'(\n\n- )(.*)', r'\n\n\\begin{itemize}\n\t\\item \2', string)
    string = re.sub(r'(\n)- (.*)(\n\n)', r'\n\t\\item \2\n\\end{itemize}\n', string)
    string = re.sub(r'\n\s?- (.*)', r'\n\t\\item \1', string)

    # Ordered Lists
    string = re.sub(r'(\n\n[0-9]\. )(.*)', r'\n\n\\begin{enumerate}\n\t\\item \2', string)
    string = re.sub(r'(\n)[0-9]\. (.*)(\n\n)', r'\n\t\\item \2\n\\end{enumerate}\n', string)
    string = re.sub(r'\n\s?[0-9]\. (.*)', r'\n\t\\item \1', string)

    string = re.sub(r'(\n\n[a-z]\. )(.*)', r'\n\n\\begin{enumerate}\[label=\\alph\*\]\n\t\\item \2', string)
    string = re.sub(r'(\n)[a-z]\. (.*)(\n\n)', r'\n\t\\item \2\n\\end{enumerate}\n', string)
    string = re.sub(r'\n\s?[a-z]\. (.*)', r'\n\t\\item \1', string)

    # Referencing
    string = re.sub(r'@c:(\S*)', r'\\cite{\1}', string)
    string = re.sub(r'@(\S*:\S*)', r'\\ref{\1}', string)

    return string


if __name__ == "__main__":
    section = sys.argv[1]
    print(convert(section))
