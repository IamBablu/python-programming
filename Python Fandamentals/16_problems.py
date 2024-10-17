"""n=int(input("enter a number"))
if n%2==0:
    print(n," is even")
else:
    print(n," is odd")
"""

'''if n<0:
    print(n," is Negative")
elif n>0:
    print(n," is positive")
else:
    print(n," Zero")
'''


"""factorial=1
a=int(input("enter a number for find factorial"))
if a<0:
    print("sorry, factorial does not exist for negative number")
elif a==1 | a==0:
    print("factorial of ",a," is ",a)
else:
    for i in range(2,a+1):
        factorial=factorial*i
        i=i+1
    print("Factorial of ",a, " is ",factorial)
"""

'''b=int(input("enter a number for reversing the number "))
rev=0
while b>0:
    dig=b%10
    b=b//10
    rev=rev*10+dig
print("after reversing your number is ",rev)
'''


"""c=int(input("enter a number for number is palindrome or not "))
re=0
d=c
while c>0:
    dig=c%10
    c=c//10
    re=re*10+dig
if (re==d):
    print(d," is palindrome number")
else:
    print(d," is not palindrome number")
"""

'''e=int(input("Enter a number for find fibonacci series of "))
i=0
j=1
if e<0:
    print("Incorrect input")
elif (e==0)|(e==1):
    print(i)
else:
    for a in range(2,e):
        k=i+j
        i=j
        j=k
    print(j)
'''


"""for num in range(11):
    for z in range(num):
        print(num,end=" ")
    print(end="\n")
"""