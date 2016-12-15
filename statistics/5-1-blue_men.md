[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> About 34% of US men are in the height range required by the Blue Man Group.
>> ```python
import thinkstats2
import thinkplot
import scipy.stats
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
print((dist.cdf(73*2.54)-dist.cdf(70*2.54))*100, '% of men are in the range required by the Blue Men Group')
```
