[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> ```
import nsfg
import math
preg=nsfg.ReadFemPreg()
live=preg[preg.outcome == 1]
firsts=live[live.birthord == 1]
others=live[live.birthord!=1]
diff=others.totalwgt_lb.mean()-firsts.totalwgt_lb.mean()
varo=others.totalwgt_lb.var()
varf=firsts.totalwgt_lb.var()
no=len(others.totalwgt_lb)
nf=len(firsts.totalwgt_lb)
pooled_var=(no*varo+nf*varf)/(no+nf)
d=diff/math.sqrt(pooled_var)
print("First babies are *lighter* than other babies. Cohen's d is "+ str(d))
print("The size effect is *larger* for birthweight than for pregnancy length")
'''
