import numpy as np
import matplotlib.pyplot as mp
n=int(input("enter n no.of values="))
sum=0
for i in range(1,n):
	sum=sum+i
	r=sum
	print (r)
	i=i+1
	mp.plot(n,r)
	mp.title('sinusoidal')	
	mp.xlabel('time')
	mp.ylabel('amplitude')
mp.show( )