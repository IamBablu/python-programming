def hello():
    print("Hello World")

def add10(x):
    return x+10

def even_odd(x):
    if x%2==0:
        print(x," is even")
    else:
        print(x," is odd")

hello()
c=add10(3)
print(c)
even_odd(11)

g=lambda x:x*x*x

print(g(5))

li=[1,4,87,67,35,88,74]
final_li=list(filter(lambda x: (x%2!=0), li))
print(final_li)
final_li=list(map(lambda x: x*2, li))
print(final_li)

from functools import reduce
li=[1,2,3,4,5,6]
sum=reduce(lambda x,y: (x+y),li)
print(sum)