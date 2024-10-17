x=int(input("Enter a number :"))
match x:
    case 0:
        print("The number is 0")
    case 10:
        print("The number is 10")
    case _ if x<10:
        print("Number is less then 10")
    case _ if x<100:
        print("Number is less then 100")
    case _:
        print("Number is greater then 100")