#I have a question: I wanted to practice using Regular Expressions
#to answer these questions, but using the columns of the .csv file
#seemed to make the below simpler. Is there a reason to prefer 
#RE for problems like these? What does the code look like? 
#Note: I ended up using RegEx for Part III, where it seemed more useful

#####Q1
g=open('faculty.csv','r')
xs=g.readlines()
g.close()

degrees=[]
for i in range(1,len(xs)):
    degrees.append(xs[i].split(',')[1])

l=list(map(lambda x: x.replace('.','').strip().split(),degrees))
u=[]
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j]!='0':
            u.append(l[i][j])

s={x for x in u}
dic={d:n for d,n in [(d,u.count(d)) for d in s]}


print('There are {0} different degrees.'.format(len(dic.keys())))
for k in dic.keys():
    print('The degree {0} is held by {1} individual(s)'.format(k,dic[k]))


######Q2
######continuing the code from above
titles=[]
for i in range(1,len(xs)):
    titles.append(xs[i].split(',')[2])
titles.sort()

l=list(map(lambda x: x.replace(' is ', ' of '),titles))  #someone entered 'Associate Professor is Biostatistics'...
l.sort()

s={x for x in l}

dic={t:n for t,n in [(t,l.count(t)) for t in s]}
print('There are {0} different titles'.format(len(dic.keys())))
for t in dic.keys():
    print('There are {0} people holding the title {1}'.format(dic[t], t))


######Q3
######continuing the code from above
email=[]
for i in range(1,len(xs)):
    email.append(xs[i].split(',')[3])

l=list(map(lambda x: x.replace('\n',''),email))
print(l)


######Q4
######continuing the code from above
dom=[]
for i in range(len(l)):
    dom.append(l[i][l[i].index('@')+1:])

unique=list({x for x in dom})
print(unique)
