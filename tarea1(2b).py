import numpy as np

b=0
for i in range(0,1000):
	a = np.random.binomial(33,0.5)
	#print a
	if a ==18:
		b+=1
	i+=1

print b
