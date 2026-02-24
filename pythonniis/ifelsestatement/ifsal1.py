print("enter basic salary")
sal=int(input())
if sal>=5000:
       da=sal*0.3
       hra=sal*0.2
else:
    da=sal*0.2
    hra=sal*0.1          
total=sal+da+hra	
print("basic salary=",sal)
print("da=",da)
print("hra=",hra)
print("total salary=",total)