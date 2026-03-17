def facttest():
	print("enter a numbere")
	f=1
	no=int(input())
	while no>0:
		f=f*no
		no=no-1
	print("factorial=",f)
facttest()		