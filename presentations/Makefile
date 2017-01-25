# Start by clearing the list of suffixes
.SUFFIXES:
# Then specify our suffixes
.SUFFIXES: .tex .dvi .bib .pdf .sgml .html .m4 .md

%.tex : %.md
	pandoc -s -i --filter pandoc-citeproc -t beamer -o $*.tex $*.md

%.pdf : %.tex
	pdflatex $*.tex
	pdflatex $*.tex

clean : 
	rm *.out
	rm *.aux
	rm *.log
	rm *.snm
	rm *.toc
	rm *.nav

