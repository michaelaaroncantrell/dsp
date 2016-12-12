'''is this text blocked'''

import numpy as np

A=np.array([[1,2,3],[2,7,4]])
B=np.array([[1,-1],[0,1]])
C=np.array([[5,-1],[9,1],[6,0]])
D=np.array([[3,-2,-1],[1,2,3]])

u=np.array([6,2,-3,5])
v=np.array([3,5,-1,4])
w=np.array([[1],[8],[0],[5]])

a=6

print(u+v)
print(u-v)
print(a*u)
print(np.dot(u,v))
print(np.linalg.norm(u))
#print(A+C)
print(A-C.transpose())
print(C.transpose()+3*D)
print(np.dot(B,A))
#print(np.dot(B,A.tranpose()))
#print(np.dot(B,C))
print(np.dot(C,B))

result=B
for i in range(3):
	result=np.array(np.dot(B,result))
print(result)

print(np.dot(A,A.transpose()))
print(np.dot(D.transpose(),D))'''
