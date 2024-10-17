x = 13
if(x>13):
    print("X is a prime number.")
else:
    print("X is not a prime number.")

print("None: ",bool(None))
#Number
print("Zero:",bool(0))
print("Integer:",bool(23))
print("Float:",bool(3.142))
print("Complex:",bool(5+2j))
#String
print("Any string:",bool("Nitesh"))   
print("A string containing number:",bool("8.5"))      
print("Empty string:" ,"")
#List 
print("Empty List:",bool([]))
print("List:",bool([1,2,5,2,1,3]))  
#Tuples
print("Empty Tuple:",bool(()))
print("Tuple:",bool(("Horse", "Rhino", "Tiger")))
#Dictionary
print("Empty Dictionary:",bool({}))
print("Dictionary:",bool({"name":"Lakshmi", "age":24 ,"job":"unemployed"}))
#Set
print("Empty Set:",bool({"Mike", 22, "Science"}))