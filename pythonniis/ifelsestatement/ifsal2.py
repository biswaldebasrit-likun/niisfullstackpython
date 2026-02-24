print("enter basic salary")
sal=int(input())
da,hra=0,0
da=sal*0.3 if sal>=5000 else sal*0.2
hra=sal*0.2 if sal>=5000 else sal*0.1
total=sal+da+hra	
print("basic salary=",sal)
print("da=",da)
print("hra=",hra)
print("total salary=",total)