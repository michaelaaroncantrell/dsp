from datetime import date
from datetime import datetime
import time

########a)

date_start = '01-02-2013'    
date_stop = '07-28-2015'

day0=date_start.split('-')
day1=date_stop.split('-')
day0=list(map(int,day0))
day1=list(map(int,day1))
d0=date(day0[2],day0[0],day0[1])
d1=date(day1[2],day1[0],day1[1])
print(d1-d0)

#########b)

date_start = '12312013'  
date_stop = '05282015'  

day0=time.strftime('%Y-%m-%d', time.localtime(int(date_start))).split('-')
day1=time.strftime('%Y-%m-%d', time.localtime(int(date_stop))).split('-')
day0=list(map(int,day0))
day1=list(map(int,day1))
d0=date(day0[0],day0[1],day0[2])
d1=date(day1[0],day1[1],day1[2])

print(d1-d0)

#########c)

date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'

date_start=date_start.replace("-", " ") 
date_stop=date_stop.replace("-"," ")
date_start=datetime.strptime(date_start, '%d %b %Y')
date_stop=datetime.strptime(date_stop, '%d %b %Y')

print(str((date_stop-date_start).days)+' days')
