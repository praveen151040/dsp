r1=input("enter no of rows for mat1")
c1=input("enter no of columns for mat1")
r2=input("enter no of rows for mat2")
c2=input("enter no of columns for mat2")
if(r1==c2):
	print"matrix multiplication is possible"
print"give input for mat1"
i=0
a={}

while(i<r1):
		j=0
		while(j<c1):
			j=j+1
			k=input("enter mat1 elements")
			a[i,j]=k

		i=i+1
print a
i=0
b={}				
while(i<r2):
		j=0
		while(j<c2):
			j=j+1
			n=input("enter values of mat2")
			b[i,j]=n
		i=i+1
print b
c={}
i=0
while(i<r1):
		j=0
		while(j<c2):
			c[i,j]=0
			k=0
			while(k<r2):
				c[i,j]=c[i,j]+a[i,k]*b[k,j]
				k=k+1
			j=j+1
		i=i+1
i=0
while(i<r1):
		j=0
		while(j<c2):
			print c[i,j]
			j=j+1
		i=i+1
print(c)





