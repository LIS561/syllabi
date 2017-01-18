#!/usr/bin/python
from rdflib import *
import bibtexparser
import sys
import re

ttlfilename = str(sys.argv[1])

project = ""
newdefs = {}
regex1 = re.compile(r"([^.]+)\.ttl")
mymatch = re.search(regex1,ttlfilename)
if mymatch:
        project = mymatch.group(1)

if project:
        cldrfilename = project + ".cldr"
        cldrfile = open(cldrfilename,"w")
        defsfilename = project + ".defs"
        defsfile = open(defsfilename,"w")

l561 = Namespace("http://courseweb.ischool.illinois.edu/lis/2017sp/lis561/")
event = Namespace("http://purl.org/NET/c4dm/event.owl#")
tl = Namespace("http://purl.org/NET/c4dm/timeline.owl#")
dc = Namespace("http://purl.org/dc/terms/")
skos = Namespace("http://www.w3.org/2004/02/skos/core#")

mygraph = ConjunctiveGraph()
mygraph.parse(ttlfilename,format="n3")

wlist = []  # List of weeks
weekstart = {} # associate weeks with their starting date

for s in mygraph.subjects(RDF.type, l561.Week):
	for i in mygraph.objects(s,event.time):
	        for a in mygraph.objects(i,tl.at):
			    weekstart[str(a)] = s
deadlines = {}

for d in mygraph.subjects(RDF.type, l561.Deadline):
                            weekdue = duedate = adue = dlabel = alabel = ""
                            for o in mygraph.objects(d,RDFS.label):
                                    dlabel = str(o)
                            for o in mygraph.objects(d,l561.dueDuring):
                                    weekdue = o
                            for o in mygraph.objects(d,l561.dueDate):
                                    duedate = str(o)
                            for a in mygraph.subjects(l561.hasDeadline,d):
                                    for o in mygraph.objects(a,RDFS.label):
                                            alabel = str(o)
                                    for o in mygraph.objects(a,l561.dueDate):
                                            adue = str(o)
                            if (weekdue in deadlines.keys()):
                                    deadlines[weekdue] += "**Due:** " + dlabel + ", " + alabel + "\n\n"
                            else:
                                    deadlines[weekdue] = "**Due:** " + dlabel + ", " + alabel + "\n\n"
                            newdefs[adue] = duedate
                            
cldrfile.write("# Topic Schedule\n")

wlist = weekstart.keys()
wlist.sort()
weeknum = 0
for d in wlist:
        myweek = myconcept = required = background  = ''
	for o in mygraph.objects(weekstart[d], RDFS.label):
	      myweek = str(o)
	for s in mygraph.objects(weekstart[d],dc.subject):
	      for p in mygraph.objects(s,skos.prefLabel):
                      myconcept = str(p)
                      for q in mygraph.objects(s,l561.backgroundReading):
                              background = str(q)
                      for r in mygraph.objects(s,l561.reqReading):
                              required = str(r)
        weeknum += 1
        weekdate = 'PRES' + str(weeknum) + 'DATE'
        cldrfile.write("\n")
        cldrfile.write("### " +  myweek + ": " + weekdate + ": " + myconcept + "\n")
        cldrfile.write("\n")
        rstring = "**Required Readings:** "
        if required:
          cldrfile.write(rstring + " " + required + "\n")
          cldrfile.write("\n")
        dstring = ""
        if weekstart[d] in deadlines.keys():
                cldrfile.write(dstring + " " + deadlines[weekstart[d]] + "\n")
                cldrfile.write("\n")
        bstring = "**Further Background:** "
        if background:
          cldrfile.write(bstring + " " + background + "\n")
          cldrfile.write("\n")

if newdefs:
        for k in newdefs.keys():
                defsfile.write("define(" + k + ", " + newdefs[k] + ")dnl\n")

          
cldrfile.close()
defsfile.close()
