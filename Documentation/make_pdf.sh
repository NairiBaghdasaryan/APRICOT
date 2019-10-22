rm p*.aux
rm p*.b??
pdflatex paper.tex ; bibtex paper.aux ; pdflatex paper.tex ; pdflatex paper.tex