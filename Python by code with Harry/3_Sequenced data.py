list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)


tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)


sequence1 = range(4,14,2)
for i in sequence1:
    print(i)



dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)


#Converting string to bytes
str1 = "This is a string"
arr1 = bytes(str1, 'utf-8')
print(arr1)
arr2 = bytes(str1, 'utf-16')
print(arr2)

#Creating bytes of given size
bytestr = bytes(4)
print(bytestr)



#Converting string to bytes
str1 = "This is a string"
arr1 = bytearray(str1, 'utf-8')
print(arr1)
arr2 = bytearray(str1, 'utf-16')
print(arr2)

#Creating bytes of given size
bytestr = bytearray(4)
print(bytestr)



str1 = bytes("home", "utf-8")
memoryviewstr = memoryview(str1)
print(list(memoryviewstr[0:]))



set1 = {4, -5, 8, 3, 2.9}
print(set1)

state = None
print(type(state))