p = float(input("Enter Your principle Amount: "))
t = float(input("Enter Your given time in year: "))
r = float(input("Enter Your rate of interest: "))

def simInt(p,t,r):
    si = (p*t*r)/100
    return si

sim = simInt(p,t,r)
amount = p+sim
print("your simple interest is ",sim)
print("And total Amount is ",amount)