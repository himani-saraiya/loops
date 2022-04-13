n=int(input("enter a number"))
i=n
sum=0
while i>0:
	result=i%10
	sum=sum+result
	i=i//10
if n%sum==0:
	print(n,"harshad number")
else:
	print(n,"not a harshad number")
