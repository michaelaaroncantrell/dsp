f=open("football.csv","r")
xs=f.readlines()
f.close()
d=0
index=0
for i in range(1,len(xs)):
    if d>(int(xs[i].split(',')[5])-int(xs[i].split(',')[6])):
        d=int(xs[i].split(',')[5])-int(xs[i].split(',')[6])
        index=i
return xs[index].split(',')[0]
#I interpreted the question to be asking for the smallest difference (including negatives), not in absolute values.

