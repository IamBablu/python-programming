fruit={"apple":10,"mango":20,"banana":30,"orange":40}
print(type(fruit))
print(fruit)
print(fruit.keys())
print(fruit.values())
print(fruit["apple"])
fruit["Guava"]=50
print(fruit)
fruit["apple"]=100
print(fruit)


f1={"apple":10,"mango":20}
print(f1)
f2={"banana":30,"orange":40}
print(f2)
f1.update(f2)
print(f1)
f1.pop("orange")
print(f1)