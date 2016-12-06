# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls`     = lists subdirectories of current directory 

> >`ls -a`  = lists subdirectories of current directory, including those that begin with '.'

> >`ls -l`   = long list. includes information like date last updated, number of subdirectories in each directory.

> >`ls -lh`  = lists subdirectories, one on each line

> >`ls -lah` = lists subdirectories, including those beginning with '.', one on each line

> >`ls -t`   = lists subdirectories, sorted by time modified, most recently modified first

> >`ls -Glp` = lists subdirectories, one per line, with color.

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs takes input and executes specified functions on that input. for example: 

> > find . -name "*.txt" | xargs rm 

> > will remove all of the files in the current directory that end in '.txt'. xargs takes the output of the find command as input, and executes rm on it.

 

