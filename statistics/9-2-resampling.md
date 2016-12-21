[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

>> There was very little difference in p-values and the max test statistic between permuting and resampling. For birthweight, p=0 under both models, tsmax_resample=.097 and tsmax_permute=.104. For the two-sided test of pregnancy length, the permutation model yielded p=.178 and tsmax=.2 while the resample model yielded p=.148 with tsmax=.225.

```python
###The only code implemented was adding the following to the hypothesis.py file
###and changing `DiffMeansPermute' to `DiffMeaansResample'
###in the RunTests function and in main().
class DiffMeansResample(DiffMeansPermute):
    ###Inherits from DiffMeansPermute, Resamples instead of permuting
    def RunModel(self):
        group1, group2 = self.data
        data= thinkstats2.Resample(self.pool, len(group1)), thinkstats2.Resample(self.pool, len(group2))
        return data
