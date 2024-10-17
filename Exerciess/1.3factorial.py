num1 = int(input("Enter your Number!: "))

def fact(n):
    return 1 if (n==0 or n==1) else n*fact(n-1)

fac = fact(num1)
print("Factorial of ",num1,"is ",fac)
