from scipy.special import comb
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps
from numpy import trapz
p = 0.0
a = 0.0
b = 0.0
c = 0.0 
p1 = 0.0

#parte 2.c
#Se calcula la PDF

pdf_x = []
pdf_y = []
for r in range(0,1001):
	a = comb (33,18)*((float(r*0.001))**18)*((1-float(r*0.001))**15)
	p+=a
	pdf_x.append(r*0.001)
	r+=1
	
#print pdf_x

#print p

for r in range(0,1001):
	c = comb (33,18)*((float(r*0.001))**18)*((1-float(r*0.001))**15)
	p2 = c/p
	pdf_y.append(p2)
	p1+=p2
	r+=1
	

#print p1
#print pdf_y

#Se calcula la CDF
cdf_x = []
cdf_y = []

cdf1 = 0
cdf2 = 0
for i in range(0,1001):
	cdf1 = pdf_y[i]
	cdf2+=cdf1
	cdf_y.append(cdf2)
	cdf_x.append(i*0.001)
#	print cdf2
	i+=1

#print cdf_x

#calculo area bajo de la curva
area1 = trapz (pdf_y, dx=0.001)
area2 = simps(pdf_y, dx=0.001)
#print area1, area2

	
# parte 2.d

menor = 0.0
mayor = 0.0
for i in range(0,1001):
	if i <501:
		m = pdf_y[i]
		menor +=m	#para P(r<0.5|X)
	else:
		m = pdf_y[i]
		mayor += m	#para P(r>0.5|X)

print menor, mayor


plt.figure(1)
plt.plot(pdf_x,pdf_y, 'bo')
plt.show()

plt.figure(2)
plt.plot(cdf_x, cdf_y, 'bo')
plt.show()	
