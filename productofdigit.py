n=int(input("enter a number"))
m=1
while n>0:
	m=m+n%10
	n=n//10
print(m)
