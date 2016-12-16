[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

>> Pearson coefficient= 0.07, Spearman coefficient= .09. The scatterplot appears to confirm this very weak correlation.
>> The percentile plot shows a weak positive correlation between mother's age and birthweight for ages 15 to 25.
>> The extreme cases may be due to small sample size of mothers at age 10 and age 45.

```python
import nsfg
import numpy as np
import thinkstats2
import thinkplot
df = nsfg.ReadFemPreg()
df=df[df.outcome==1]	#live births
df=df.dropna(subset=['totalwgt_lb', 'agepreg'])

Pearson=thinkstats2.Corr(df.totalwgt_lb,df.agepreg)
print("The Pearson coefficient is ", Pearson)
Spearman=thinkstats2.SpearmanCorr(df.totalwgt_lb,df.agepreg)
print("The Spearman coefficient is ", Spearman)

#thinkplot.Scatter(df.totalwgt_lb,df.agepreg)				#uncomment these to
#thinkplot.Show(xlabel='birthweight',ylabel="Mother's Age")		#see scatterplot

bins=np.arange(10,50,2.5)
indices=np.digitize(df.agepreg,bins)
groups=df.groupby(indices)

ages=[group.agepreg.mean() for i, group in groups]
cdfs=[thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]

for percent in [75,50,25]:
	weights=[cdf.Percentile(percent) for cdf in cdfs]
	label='{0}dth'.format(percent)
	thinkplot.Plot(ages, weights, label=label)

thinkplot.Show()
