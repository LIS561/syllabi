# Start by clearing the list of suffixes
.SUFFIXES:
# Then specify our suffixes
.SUFFIXES: .tex .dvi .bib .pdf .sgml .html .m4 .md

M4PATH := ./md
export M4PATH

%.md : %.m4 template1.m4
	m4 -DFORMATDEFS="wpformat.m4" -DMYDEFS="$*.m4" template1.m4 > $*.md

%.docx : %.md template.bib
	pandoc -s --bibliography=template.bib -o $*.docx $*.md

%.html : %.md template.bib
	pandoc -s --bibliography=template.bib -o $*.html $*.md

