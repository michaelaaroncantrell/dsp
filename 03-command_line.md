# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > pwd = prints the directory you are currently in

> > mkdir = makes a new directory

> > cd = the way to move between directories

> > ls = list directory. what directories lie in the current directory

> > rmdir = remove directory. this won't work if the directory has other files in it, unless you override with 'rm -rf'. careful! you lose the contents inside the directory

> > rm = remove file

> > cp = copy a file or directory. you can specify where to put the copy

> > mv = move a file or directory. really just renaming, but deletes the current instance

> > less = read through a file using space and w to page down and up

> > cat = read the whole file. prints in terminal. may include multiple files

> > xargs = takes input and executes specified function on the input. see example of deleting all .txt files below

> > find = find files. the wildcard * is useful here, e.g. to find all text files.

> > grep = find lines containing a string (or not containing the string) in specified files

> > man = this followed by a command jumps to the manual chapter describing said command

> > echo = print some arguments

> > | = pipes from left to right

> > < = sends input from left to program on right

> > '>' = sends output from left to program on right

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

> > ls -R = displays subdirectories as well

> > ls -m = displays as comma separated list

> > ls -a = displays all files

> > ls -1 = displays one entry per line

> > ls -c = displays by timestamp 

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs takes input and executes specified functions on that input. for example: 

> > find . -name "*.txt" | xargs rm 

> > will remove all of the files in the current directory that end in '.txt'. xargs takes the output of the find command as input, and executes rm on it. 

 

