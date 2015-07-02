# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:42:37 2015

@author: bpafoshizle
"""

import survey
import numpy

table = survey.Pregnancies()
table.ReadRecords()
print('Number of pregnancies', len(table.records))

liveBirthCount = 0
for rec in table.records:
    if(rec.outcome == 1):
        liveBirthCount = liveBirthCount + 1        
print("The number of live births:%s" % liveBirthCount)
print("The number of live births list comprehension: %s" % \
   sum([rec.outcome for rec in table.records if rec.outcome == 1]))

firstBabies = survey.Pregnancies()
others = survey.Pregnancies()
for rec in table.records:
    if(rec.birthord == 1):
        firstBabies.AddRecord(rec)
    else:
        if(rec.outcome == 1):
            others.AddRecord(rec)

print("First babies:%s" % len(firstBabies))
print("Others:%s" % len(others))

muFirst = numpy.mean([rec.prglength for rec in firstBabies.records])
muOthers = numpy.mean([rec.prglength for rec in others.records])
print("First babies: %s" % muFirst)
print("Others: %s" % muOthers)
print("Difference in means: %s" % ((muFirst - muOthers)*7))


#import urllib2
#url = "http://greenteapress.com/thinkstats/first.py"
#with open("first.py", "wb") as f:
#    f.write(urllib2.urlopen(url).read())