#!/usr/bin/python
from rdflib import *
import bibtexparser
import sys

calfilename = str(sys.argv[1])

l561 = Namespace("http://courseweb.ischool.illinois.edu/lis/2017sp/lis561/")
event = Namespace("http://purl.org/NET/c4dm/event.owl#")
tl = Namespace("http://purl.org/NET/c4dm/timeline.owl#")
dc = Namespace("http://purl.org/dc/terms/")
skos = Namespace("http://www.w3.org/2004/02/skos/core#")

mygraph = ConjunctiveGraph()
mygraph.parse(calfilename,format="n3")

wlist = []  # List of weeks
weekstart = {} # associate weeks with their starting date

for s in mygraph.subjects(RDF.type, l561.Week):
	for i in mygraph.objects(s,event.time):
	        for a in mygraph.objects(i,tl.at):
			    weekstart[str(a)] = s
deadlines = {}

for d in mygraph.subjects(RDF.type, l561.Deadline):
                            weekdue = duedate = dlabel = alabel = ""
                            for o in mygraph.objects(d,RDFS.label):
                                    dlabel = str(o)
                            for o in mygraph.objects(d,l561.dueDuring):
                                    weekdue = o
                            for o in mygraph.objects(d,l561.dueDate):
                                    duedate = str(o)
                            for a in mygraph.subjects(l561.hasDeadline,d):
                                    for o in mygraph.objects(a,RDFS.label):
                                            alabel = str(o)
                            deadlines[weekdue] = dlabel + ", " + alabel + ", Due " + duedate
print "# Topic Schedule"

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
        print                      
        print "## " +  myweek + ": " + weekdate + ": " + myconcept
        print
        rstring = "Required Readings: "
        if required:
          print rstring
          print
          print ":  " + required
          print
        dstring = "Due this week: "
        if weekstart[d] in deadlines.keys():
                print dstring
                print
                print ":  " + deadlines[weekstart[d]]
                print
        bstring = "Further Background: "
        if background:
          print bstring
          print
          print ":  " + background




        
	 

