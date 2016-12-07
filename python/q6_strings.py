# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
	if count<10:
		return 'Numbers of donuts: '+str(count)
	else:
		return 'Number of donuts: many'


def both_ends(s):
	if len(s)<=1:
        	return ''
   	return s[:2]+s[len(s)-2:]


def fix_start(s):
   	return s[0]+(s[1:].replace(s[0],'*'))
    

def mix_up(a, b):
    	return b[:2]+a[2:]+' '+a[:2]+b[2:]
  

def verbing(s):
    	if len(s)<3:
        	return s
    	elif s[len(s)-3:]=='ing':
       		return s+'ly'
  	else:
        	return s+'ing'


def not_bad(s):
   	b=s.find('bad')
   	n=s.find('not')
   	if b<n:
      		return s
    	else:
        	return s[:n]+'good'+s[b+3:]
        

def front_back(a, b):
   	 a_front=a[:len(a)//2+len(a)%2]
   	 a_back=a[len(a)//2+len(a)%2:]
   	 b_front=b[:len(b)//2+len(b)%2]
   	 b_back=b[len(b)//2+len(b)%2:]
  	 return a_front+b_front+a_back+b_back
	
