num = int(input("Enter a number tile where your want to print prime number: "))
def pri(n):
    for i in range(n+1):
        if i>1:
            for j in range(2,i):
                if (i%j==0):
                    break
            else:
                print(i,end=" ")
pri(num)