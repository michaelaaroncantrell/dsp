[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>>The bias makes a real impact. The bias pmf mean is 2.4 compared to the actual pmf mean of 1.0.

```python
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
