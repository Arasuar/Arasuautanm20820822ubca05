def fact(x):
	if x==0 or x==1:
		return 1
	else:
		return x*fact(x-1)
	
n=int(input("enter a number : "))
factorial=fact(n)
print("%d factorial value is  %d"%(n,factorial))