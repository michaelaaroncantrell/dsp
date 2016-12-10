def match_ends(words):
    return len(list(filter(lambda w: (len(w)>1 and w[0]==w[len(w)-1]), words)))
    

def front_x(words):
    def compare(a,b):
        if a[0]=='x' and b[0]!='x':
            return -1
        if a[0]!='x' and b[0]=='x':
            return 1
        else:
            if a<b:
                return -1
            elif b<a:
                return 1
            else:
                return 0
    words.sort(cmp=compare)
    return words



def sort_last(tuples):
    def last(x):
        return x[len(x)-1]
    return tuples.sort(key=last)
    
 

def remove_adjacent(nums):
    return [nums[i] for i in range(len(nums)) if i==0 or nums[i-1]!=nums[i]]
   


def linear_merge(list1, list2):
    l=[]
    while len(list1)>0 and len(list2)>0:
        if list1[0]<list2[0]:
            l.append(list1.pop(0))
        else:
            l.append(list2.pop(0))

    l.extend(list1)
    l.extend(list2)
    return l
