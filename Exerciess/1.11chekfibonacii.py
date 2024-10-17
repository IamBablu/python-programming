num = int(input("Enter a number: "))
def fibonacci(n):
    if n==0 or n==1:
        return n
    else :
        return fibonacci(n-1)+fibonacci(n-2)

if num ==0 or num ==1:
    print(num,"is a fibonacci number")
else:
    for i in range(2,num+2):
        result = fibonacci(i)
        # print(result)
        if result==num:
            print(num,"is a fibonacci number")
            break
    else:
        print(num,"is not a fibonacci number")
        