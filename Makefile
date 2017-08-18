# Start by clearing the list of suffixes
.SUFFIXES:
# Then specify our suffixes
.SUFFIXES: .tex .dvi .bib .pdf .sgml .html .m4 .md

M4PATH := ./md
export M4PATH

%.md : %.m4 %.cldr %.defs LIS561.m4
	m4 -DFORMATDEFS="wpformat.m4" -DMYDEFS="$*.m4" LIS561.m4 > $*.md

%.docx : %.md LIS561.bib
	pandoc -s --bibliography=LIS561.bib -o $*.docx $*.md

%.html : %.md LIS561.bib
	pandoc -s --bibliography=Readings.bib -o $*.html $*.md

%.cldr : %.ttl 
	 python NewCalendar2.py $*.ttl

%.defs : %.ttl 
	 python NewCalendar2.py $*.ttl


