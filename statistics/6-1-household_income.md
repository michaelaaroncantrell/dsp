[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

>> The mean is $45455. The median is $51226. In log_10 units, we have Pearson's skew= -0.73, the Skewness= -6.55, and about 45% of households have income below the mean.

```python
import numpy as np

import hinc
import thinkplot
import thinkstats2

def InterpolateSample(df, log_upper=6.0):       ###this part is copied from the author
    df['log_upper'] = np.log10(df.income)
    df['log_lower'] = df.log_upper.shift(1)
    df.log_lower[0] = 3.0
    df.log_upper[41] = log_upper
    arrays = []
    for _, row in df.iterrows():
        vals = np.linspace(row.log_lower, row.log_upper, row.freq)
        arrays.append(vals)
    log_sample = np.concatenate(arrays)
    return log_sample
    
df = hinc.ReadData()              
log_sample = InterpolateSample(df, log_upper=6.0)
log_cdf = thinkstats2.Cdf(log_sample)           ###Up to here is copied from author

pdf=thinkstats2.EstimatedPdf(log_sample)
thinkplot.Pdf(pdf, label='income')

mean=log_sample.mean()
median=log_cdf.Value(.5)
std=log_sample.var()

def RawMoment(xs, k):
    return sum(x**k for x in xs) / len(xs)
def CentralMoment(xs, k):
    mean = RawMoment(xs, 1)
    return sum((x - mean)**k for x in xs) / len(xs)

print("{0} percent of households have income below the mean".format(log_cdf.PercentileRank(mean)))
print("Pearson's skew is {0}".format(3*(mean-median)/std))
print("The Skewness is", CentralMoment(log_sample,3)/std**3)
