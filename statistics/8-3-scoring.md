[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

---

>> For a sample size of 1000000 I observed a Mean Error of 1 and a RMS Error of 1.7. The Mean
>> Error does decrease with increasing sample size, albeit very slowly. I am not convinced this 
>> is an unbiased estimator (though the author is). Since goals scored is discrete and often 
>> close to 0, the 90 percent confidence interval for the estimator of, say, 2, is pretty meaningless.
>> It is (1,6). I think smoothing the distribution might be helpful here (allowing for fractional
>> scores).

```python
import thinkstats2
import thinkplot

import math
import random
import numpy as np

def RMSE(estimates, actual):
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)

def MeanError(estimates, actual):
    errors = [estimate-actual for estimate in estimates]
    return np.mean(errors)

def goals(lam):
    t=0
    count=0
    while t<1:
        d=random.expovariate(lam)
        count+=1
        t+=d
    return count

def estimate(lam=2, m=1000000):

	outcomes=[]
	for _ in range(m):
		outcomes.append(goals(lam))
	print("Mean Error is ", MeanError(outcomes,lam))
	print("RMS Error is ", RMSE(outcomes,lam))
	cdf=thinkstats2.Cdf(outcomes)
	lower=cdf.Value(.05)
	upper=cdf.Value(.95)
	print("90 percent confidence interval", (lower,upper))
	thinkplot.Cdf(cdf)
	thinkplot.Show(xlabel='goals', ylabel='CDF')

estimate()

---
