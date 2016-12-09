#####Q6
import re
g=open('faculty.csv','r')
xs=g.readlines()
g.close()
xs=list(map(lambda x: x.replace('\n',''),xs)) #get rid of '\n'

dic={}
p=re.compile(r'\b\w*\b$')                     #matches last word
q=re.compile('.*Professor')                   #matches everything up to 'Professor'

for i in range(1,len(xs)):
    entry=xs[i].split(',')

    newtitle=q.search(entry[2]).group() #update entry so that 
    entry[2]=newtitle                   #titles ends at 'Professor'
  
    lastname=p.search(entry[0]).group()
    data=[x for x in entry[1:]]
    info=dic.get(lastname,[])
    info.append(data)
    dic[lastname]=info

print(sorted(list(dic.items())))

#####Q7
#####Continuing the code from above

f=re.compile(r'\w*')                    #matches first word in string
d2={}
for i in range(1,len(xs)):
    entry=xs[i].split(',')

    newtitle=q.search(entry[2]).group() #update entry so that 
    entry[2]=newtitle                   #titles ends at 'Professor'
    entry[1]=entry[1][1:]               #remove white space at beginning of degrees

    lastname=p.search(entry[0]).group()
    firstname=f.search(entry[0]).group()
    data=[x for x in entry[1:]]
    d2[(firstname,lastname)]=data

print(sorted(d2.items()))

######Q8
######Continuing the code from above

print(sorted(d2.items(),key=lambda x: x[0][1]))






    








