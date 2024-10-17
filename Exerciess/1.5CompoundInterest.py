p = float(input("Enter Your principle Amount: "))
t = float(input("Enter Your given time period: "))
r = (float(input("Enter Your rate of interest in present: ")))/100 #diving by 100 for removing %
n = int(input("Enter number of times interest applied per time period: "))

def comInt(p,t,r,n):
    Amount = p*(pow((1+r/n),(n*t)))
    Ci = Amount - p
    print("Your Compound Interest is",round(Ci,3),"and total amount is",round(Amount,2))

comInt(p,t,r,n)
