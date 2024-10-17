num = int(input("Enter your Number!: "))

def isArmstrong(n):
    m = n
    sum = 0
    while(n>0):
        sum = (sum*10)+n%10
        n = n//10
    if m==sum :
        print(m,"is an Armstrong number")
    else:
        print(m,"is not an Armstrong number")

isArmstrong(num)
print(order(num))