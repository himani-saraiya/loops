w=(input("enter a word"))
l=(input("enter a latter"))
i=0
count=0
while i<len(w):
	if (w[i]==l):
		count=count+1
	i=i+1
print(count)	