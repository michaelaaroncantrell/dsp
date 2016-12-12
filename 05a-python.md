# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are sequences, i.e. they maintain order. So one may index them, e.g. ```l[1]```. Both have membership, concatenation with + and *, and enumerate.

>> The main difference is that tuples, like strings, are immutable, while lists are mutable. Tuple doesn't have a length function. List has many built in methods, due to its mutability. One of the most prominent is item assignment. Others include, sort, append, insert, count, extend, index and remove.

>> Tuples work as keys in a dictionary, basically because they are immutable. The mutability of lists could confuse the dictionary.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> The main difference between lists and sets is that lists are ordered and may contain multiple entries of the same item, while sets are not ordered, and may only contain one entry of any item. Sets also have built-in set theoretic methods, like union, intersection, difference, and symmetric difference (lists don't). 

>> Both sets and lists are mutable, and have similar updating methods, though some of their names are different, since there is/is not order. For example, set has add, remove, and pop, while list has insert/append, remove, and pop.

>> You might use a list to enter your students' test scores, so that you can sort them. If you want to compare which countries you and your friends have been to, you might create a set for each person.

>> Sets are considerably faster for determining membership because they use 'hashing', which I haven't tried to understand.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The lambda function is an anonymous, one use, in line defined function. It is used to accomplish a task that likely will not be repeated, and is typically small.

>> The next example prints those numbers from 1 to 24 that are multiples of 3 or 5. 

>> ```print(list(filter(lambda x: x%3==0 or x%5==0 , range(1,25))))```  

>> The next example prints the length of the words in a sentence.

>> ```s="This is an example sentence".split()  
>> print(list(map(lambda word: len(word), s)))``` 

>> Here is an example using 'lambda' in the 'key' argument to 'sorted'. The list is a list of tuples, with a student's name, major, and gpa. The code sorts the students by their gpa, with the highest gpa first.

>> ```students=[('Amy', 'Chemistry', '3.7'), ('Bob', 'Chemistry', '2.2'), ('Carol','Physics','4.0')]

>>print(sorted(students, key=lambda student: student[2], reverse=True))```

>> We could similarly use key=lambda here to sort by any of the indices in the tuple, e.g. the students in alphabetic order.

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is a way to construct a list using a for statement followed by zero or more for and in statements. They read just like mathematics, and are more concise than traversing a list and appending entries one by one.

>> For example, $[(i,i**2) for i in range(10)] would create a list of tuples of  numbers from 0 to 9 together with their squares.

>> $[(x,y) for x in [1,2,3] for y in [2,3,4] if x!=y] creates a list of all pairs of tuples from the two lists without any 'diagonal' terms, where x and y are equal.

>> A list comprehension could be used in place of the following example using 'map'. $map(len, "This is a sentence".split()).

>> Instead, $[len(w) for w in "This is a sentence".split()]

>> A list comprehension could be used in place of the following example using 'filter' $list(filter(lambda x: x%2==0,range(1,7)))

>> Instead, $[x for x in range(1,7) if x%2==0].

>> Comparison: filter and map may be applied to any iterables, e.g. strings, tuples, while list comprehension only works on list. That being said, it seems to me that any filter or map operation on a list could be done with list comprehension. Is this correct? 

>> Set comprehension: ${x for x in range(10) if x%3!=0}

>> Dictionary comprehension: ${k:v for k,v in [(i,i**2) for i in range(5)]}

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> -82 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





