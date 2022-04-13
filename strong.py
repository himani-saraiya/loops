x=int(input("enter a number"))
i=0
b=x
total=0
while b:
	i=b%10
	c=1
	while i:
		c=c*i
		i=i-1
	total=total+c
	b=b//10
if total==x:
		print("strong number")
else:
		print("no")