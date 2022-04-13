a=int(input("enter a no."))
b=int(input("enter a no."))
i=1
while i>0:
	if a>b:
		print(a,"largest")
		print(b,"smallest")
	elif a<b:
		print(a,"smallest")
		print(b,"largest")
	else:
		print("equal")
	break
	i=i+1