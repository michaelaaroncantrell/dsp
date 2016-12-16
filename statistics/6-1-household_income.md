[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

>> The mean is $74278. The median is $51226. Pearson's skew= 0.74, Skewness= 4.9, and about 66% of households have income below the mean. If the assumed upper bound were larger, then the distribution would extend to the right more, increasing the right-skewedness.

```python
from __future__ import print_function
import numpy as np
import math
import hinc
import thinkplot
import thinkstats2
def InterpolateSample(df, log_upper=6.0):
    """Makes a sample of log10 household income.

    Assumes that log10 income is uniform in each range.

    df: DataFrame with columns income and freq
    log_upper: log10 of the assumed upper bound for the highest range

    returns: NumPy array of log10 household income
    """
    # compute the log10 of the upper bound for each range
    df['log_upper'] = np.log10(df.income)

    # get the lower bounds by shifting the upper bound and filling in
    # the first element
    df['log_lower'] = df.log_upper.shift(1)
    df.log_lower[0] = 3.0

    # plug in a value for the unknown upper bound of the highest range
    df.log_upper[41] = log_upper

    # use the freq column to generate the right number of values in
    # each range
    arrays = []
    for _, row in df.iterrows():
        vals = np.linspace(row.log_lower, row.log_upper, row.freq)
        arrays.append(vals)

    # collect the arrays into a single sample
    log_sample = np.concatenate(arrays)
    return log_sample


df = hinc.ReadData()
log_sample = InterpolateSample(df, log_upper=6.0)               ###Code up to here is from author
sample = np.power(10, log_sample)
cdf = thinkstats2.Cdf(sample)

mean=sample.mean()
median=cdf.Value(.5)
std=math.sqrt(sample.var())

def RawMoment(xs, k):
    return sum(x**k for x in xs) / len(xs)
def CentralMoment(xs, k):
    mean = RawMoment(xs, 1)
    return sum((x - mean)**k for x in xs) / len(xs)

print("The mean and median, in dollars, are",mean,median)
print("The std is",std)
print("{0:.0f} percent of households have income below the mean".format(cdf.PercentileRank(mean)))
print("Pearson's skew is {0}".format(3*(mean-median)/std))
print("The Skewness is", CentralMoment(sample,3)/std**3)

pdf=thinkstats2.EstimatedPdf(sample)
thinkplot.Pdf(pdf, label='income')
thinkplot.Show()
