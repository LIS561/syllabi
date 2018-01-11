# Start by clearing the list of suffixes
.SUFFIXES:
# Then specify our suffixes
.SUFFIXES: .tex .dvi .bib .pdf .sgml .html .m4 .md

M4PATH := ./md
export M4PATH

%.md : %.m4 %.cldr %.defs IS561.m4
	m4 -DFORMATDEFS="wpformat.m4" -DMYDEFS="$*.m4" IS561.m4 > $*.md

%.docx : %.md %.bib
	pandoc -s --bibliography=$*.bib -o $*.docx $*.md

%.bib : currentReadings.bib
	cat currentReadings.bib > $*.bib

%.ttl : turtlePrefixes currentCalendar %.topics %.sched 
	cat turtlePrefixes currentCalendar $*.topics $*.sched > $*.ttl

%.cldr : %.ttl 
	 python NewCalendar2.py $*.ttl

%.defs : %.ttl 
	 python NewCalendar2.py $*.ttl


