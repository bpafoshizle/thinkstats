# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 21:16:27 2015

@author: bpafoshizle
"""


def Pumpkin():
   import thinkstats
   import math
   t = [1, 1, 1, 3, 3, 591]
   mu, var = thinkstats.MeanVar(t)
   sd = math.sqrt(var)
   return mu, var, sd


print("Mean: %s, Var: %s, StDv: %s" % Pumpkin())

def StdDevGest():
    import first
    table, firsts, others = first.MakeTables()
    first.ProcessTables(firsts, others)
    
    print("Mean Firsts: %s, StDv Firsts: %s" % (firsts.mu, firsts.stdv))
    print("Mean Others: %s, StDv Others: %s" % (others.mu, others.stdv))
    
StdDevGest()

#with open("Pmf.py", "wb") as f:
#    import urllib2
#    f.write(urllib2.urlopen("http://greenteapress.com/thinkstats/Pmf.py").read())

def Mode(hist):
    idx = hist.Freqs().index(sorted(hist.Freqs(), reverse=True)[0])
    return hist.Values()[idx]

def AllModes(hist):
    from operator import itemgetter
    return sorted(hist.Items(), reverse=True, key=itemgetter(1))
    

import Pmf
hist = Pmf.MakeHistFromList([1, 2, 2, 3, 5])
Mode(hist)
AllModes(hist)

def RemainingLifetime(pmf, age):
    d = [{val, prob} for val, prob in pmf.Items() if val > age]
    return Pmf.MakePmfFromDict(d)
 
def PmfMean(pmf):
    return sum([prob * val for val, prob in pmf.Items()])
    
def PmfVar(pmf):
    mu = PmfMean(pmf)
    return sum([prob * (val - mu)**2 for val, prob in pmf.Items()])

def comparePmfMehtods():
    import first 
    table, firsts, others = first.MakeTables()
    first.ProcessTables(firsts, others)
    
    firstsPmf = Pmf.MakePmfFromList(firsts.lengths)
    
    print("firstsPmf.Mean():%f2" % firstsPmf.Mean())
    print("PmfMean(firstsPmf):%f2" % PmfMean(firstsPmf))
    
    print("firstsPmf.Var():%f2" % firstsPmf.Var())
    print("PmfVar(firstsPmf):%f2" % PmfVar(firstsPmf))
    
    
def downloadDescriptive():
    with open("descriptive.py", "wb") as f:
        import urllib2
        f.write(urllib2.urlopen("http://thinkstats.com/descriptive.py").read())





    