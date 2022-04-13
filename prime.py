n=int(input("enter any number"))
i=1
c=0
while i<=n:
	if n%i==0:
		c=c+1
	i+=1
if c==2:
	print(n,'prime number')
else:
	print("not")