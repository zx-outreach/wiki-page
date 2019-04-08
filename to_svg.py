import os
import subprocess
import time


TEX = r"""\documentclass[tikz,convert={outfile=svg/replaceme.svg}]{standalone}
\usepackage{tikzit}
\input{zx.tikzdefs}
\input{zx.tikzstyles}

\begin{document}
\tikzfig{replaceme}
\end{document}"""

for figure in os.listdir("figures"):
    if figure.endswith(".tikz"): 
        figname = figure[:-5]
        f = open("convert_this.tex",'w')
        tex = TEX.replace("replaceme",figname)
        print(tex)
        f.write(tex)
        f.close()
        time.sleep(0.1)
        print("Processing", figure)
        subprocess.call(["pdflatex", "--shell-escape", "convert_this.tex"])
        
