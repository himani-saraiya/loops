n=int(input("enter a number"))
sum=0
i=1
while n!=0:
	r=n%10
	sum=sum+r*pow(2,1)
	n=int(n/10)
	i=i+1
print("decemal num",sum)