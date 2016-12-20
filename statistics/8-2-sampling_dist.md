[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

>> The standard error tends to 0 as the sample size tends to infinity. The 90% confidence interval always contains the actual value of 2, and shrinks as the sample size tends to infinity.

```python
from __future__ import print_function
import thinkstats2
import thinkplot
import math
import random
import numpy as np

def RMSE(estimates, actual):
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)
####UP TO HERE IS COPIED FROM AUTHOR####    
lam=2
v=[10,50,100,500,1000,5000]
SEs=[]
for n in v:
    estimates=[]
    for i in range(1000):
       xs=np.random.exponential(1.0/lam, n)
       L=1/np.mean(xs)
       estimates.append(L)

    SE=RMSE(estimates,lam)
    SEs.append(SE)
    cdf=thinkstats2.Cdf(estimates)
    thinkplot.Cdf(cdf, label=n)
    lower=cdf.Value(.05)
    upper=cdf.Value(.95)
    print("The 90 percent confidence interval for n=", n, (lower,upper))
    print("The SE with sample size", n, "is", SE)
thinkplot.preplot(5)
cdf=thinkstats2.Cdf(estimates)
thinkplot.Cdf(cdf)
#uncomment this to see the sampling distribution of the estimate for lambda. #thinkplot.Show()
thinkplot.plot(v,SEs)
thinkplot.Show(xlabel='sample size', ylabel='SE')
