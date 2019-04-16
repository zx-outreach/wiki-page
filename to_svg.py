import os
import subprocess
import time


TEX = r"""\documentclass[tikz]{standalone}
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
        #print(tex)
        f.write(tex)
        f.close()
        time.sleep(0.1)
        print("Processing", figure)
        subprocess.call(["latex", "convert_this.tex"])
        time.sleep(0.4)
        subprocess.call(["dvisvgm", "convert_this.dvi"])
        os.rename("convert_this.svg","svg\\{}.svg".format(figname))
        
