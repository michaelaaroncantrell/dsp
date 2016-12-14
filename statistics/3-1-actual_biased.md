[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> There is clear bias. The mean for the biased pmf is 2.403, compared to 1.024 for the actual pmf.
```
import chap01soln
resp = chap01soln.ReadFemResp()

import thinkplot
import thinkstats2
pmf=thinkstats2.Pmf(resp.numkdhh, label='numkdhh actual')

def BiasPmf(pmf, label=''):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf

biaspmf=BiasPmf(pmf, label='numkdhh bias')

realmean=pmf.Mean()
print(realmean)	#1.024

biasmean=biaspmf.Mean()
print(biasmean)	#2.403

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf,biaspmf])
thinkplot.Show(xlabel='number of kids in household')
```
