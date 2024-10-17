name="Abhishek"  #type str
age=27           #type int
passed=True      #type bool
NameOfCity="Mumbai"    #Pascal case
nameOfCity="Berlin"    #Camel case
name_of_city="Moscow"  #Snake case
icecream = "Vanilla"    #global variable
def foods():
    vegetable = "Potato"    #local variable
    fruit = "Lichi"         #local variable
    print(vegetable + " is a local variable value.")
    print(icecream + " is a global variable value.")
    print(fruit + " is a local variable value.")

foods()
print(icecream + " is a global variable value.")
#print(fruit + " is a local variable value.")# because it is a local variable
