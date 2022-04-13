n=int(input("enter a number"))
i=1
sum=0
while i<=n//2:
	if n%i==0:
		sum=sum+i
	i=i+1
if sum==n:
	print(n,"perfect number")
else:
	print(n,"not a perfect number")
