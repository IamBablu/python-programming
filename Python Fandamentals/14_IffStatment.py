a=10
b=20
if a>b:
    print("a is greater")
else:
    print("b is greater")

c=30
if (a>b)&(a>c):
    print("a is greatest")
elif (b>a)&(b>c):
    print("b is greatest")
else:
    print("c is greatest")


tup=(1,2,3,4,"a")
if "a" in tup:
    print("a is present in tup")
else:
    print("a is not present in tup")

    
if 7 in tup:
    print("7 is present in tup")
else:
    print("7 is not present in tup")
    
list=[1,2,3,4,5]
if list[0]==1:
    list[1]=100
print(list)

dis={"k":10,"b":100,"n":50}
if dis["k"]==10:
    dis["k"]=dis["k"]+100
print(dis)

