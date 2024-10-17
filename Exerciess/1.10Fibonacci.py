num = int(input("Enter a number: "))
def fibonacci(n):
    if n==0 or n==1:
        return n
    else :
        return fibonacci(n-1)+fibonacci(n-2)

fibNumber = fibonacci(num)
print(f"{num}th fibonacci number is:",fibNumber)