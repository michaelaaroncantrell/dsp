import numpy as np

A=np.array([[1,2,3],[2,7,4]])
B=np.array([[1,-1],[0,1]])
C=np.array([[5,-1],[9,1],[6,0]])
D=np.array([[3,-2,-1],[1,2,3]])

u=np.array([6,2,-3,5])
v=np.array([3,5,-1,4])
w=np.array([[1],[8],[0],[5]])

a=6

print(u+v) 					# [9  7 -4  9]
print(u-v) 					# [ 3 -3 -2  1]
print(a*u) 					# [ 36  12 -18  30]
print(np.dot(u,v))				# 51
print(np.linalg.norm(u))			# 8.60232526704
#print(A+C)					# not defined
print(A-C.transpose())				# [[-4 -7 -3],[ 3  6  4]]
print(C.transpose()+3*D)			# [[14  3  3],[ 2  7  9]]
print(np.dot(B,A))				# [[-1 -5 -1],[ 2  7  4]]
#print(np.dot(B,A.tranpose()))			# not defined
#print(np.dot(B,C))				# not defined
print(np.dot(C,B))				# [[ 5 -6],[ 9 -8],[ 6 -6]]

result=B
for i in range(3):
	result=np.array(np.dot(B,result))
print(result)					# [[ 1 -4],[ 0  1]]

print(np.dot(A,A.transpose()))			# [[14 28],[28 69]]
print(np.dot(D.transpose(),D))			# [[10 -4  0],[-4  8  8],[ 0  8 10]]
