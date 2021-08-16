 # interpolate from dataset at node value and use gaussian quadrature for integration

import math
import numpy as np
import scipy
from scipy import integrate


x = np.zeros(5000)  # Dataset of time
y = np.zeros(5000)  # Dataset of blank
z = np.zeros(5000)  # Dataset of correlation
c = np.zeros(10)     # Dataset of node point
w = np.zeros(10)     # Weight
d = np.zeros(10)     # Interpolated Data at scaled-node point for t*c(t)
g = np.zeros(10)     # Interpolated data at scaled node point for c(t)
p = np.zeros(10)     # scaled data point of nodes
m = np.zeros(10)     # Blank
q =[]
# a_1,b_1,c_1 data stored upto 100 nanosecond
a_1 = np.zeros(5000)
b_1 = np.zeros(5000)
c_1 = np.zeros(5000)
f = open('list','r')
f4 = open('ouput','w')
f6 = open('output-corr51','w')
for i in range(2):
	s = f.readline()
        token = s.split()
	q.append(token[0])
	#print q[i]


def f(h,h1,a,b):
	summ,summ1 = 0.0,0.0
	for j in range(10):
		p[j] = h*c[j] + h1
		g[j] = np.interp(p[j], x, z)		
		summ1 = summ1 + g[j]*w[j]
		
	return summ1
f2 = open('10pt-gaussian.dat','r')

# Reading data of 10pt-gaussian quadrature

for j in range(10):
	s1 = f2.readline()
	token = s1.split()
	m[j] = token[0]
	w[j] = token[1]
	c[j] = token[2] 





# Reading data of correlation point	
summ1 = 0.0
for k in range(2):
	f1 = open(q[k],'r')
	inte = 0.0
	for i in range(5000):
		s = f1.readline()
		token = s.split()
		x[i] = token[0]
		#y[i] = token[1]
		z[i] = token[1]
	a = x[0]
	b = x[4999]
	#print a,b
	h = (b-a)/2	
	h1 = (b+a)/2
	inte = inte + f(h,h1,a,b)
	summ1 = summ1 + h*inte
	print >> f4,q[k], 2*h*inte
print >> f4, 2*summ1,'		', -22.8*summ1
print >> f6,2*summ1,'		', -22.8*summ1





	
