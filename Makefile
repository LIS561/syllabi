# Start by clearing the list of suffixes
.SUFFIXES:
# Then specify our suffixes
.SUFFIXES: .tex .dvi .bib .pdf .sgml .html .m4 .md

M4PATH := ./md
export M4PATH

%.md : %.m4 %.cldr LIS561.m4
	m4 -DFORMATDEFS="wpformat.m4" -DMYDEFS="$*.m4" LIS561.m4 > $*.md

%.docx : %.md LIS561.bib
	pandoc -s --bibliography=LIS561.bib -o $*.docx $*.md

%.html : %.md LIS561.bib
	pandoc -s --bibliography=LIS561.bib -o $*.html $*.md

%.cldr : %.ttl 
	./NewCalendar2.py $*.ttl > $*.cldr


