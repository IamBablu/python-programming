# lst1 = [1,2,3,4,5]
# lst2 = ["green", "red", "blue"]
# print(lst1)
# print(lst2)


# list = ["abhisekh",3,"bablu",4]
# print(list)

# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# print(colors[1])
# print(colors[3])
# # print(colors[5])-->it willl be throw error because colors hasno't index 5
# print(colors[-1])
# print(colors[-3])

# if "Yellow" in colors:
#     print("Yellow present in colors")
# else:
#     print("Yellow not present")


# if "yellow" in colors:
#     print("yellow present in colors")
# else:
#     print("yellow not present")


# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[3:7])	#using positive indexes
# print(animals[-7:-2])	#using negative indexes
# print(animals[4:])
# print(animals[:-4])
# print(animals[2:6:2])
# print(animals[::2])
# print(animals[-8:7:2])


# colors = ["voilet", "indigo", "blue"]
# colors.append("Green")
# print(colors)
# colors.insert(1,"Orange")
# print(colors)
# rainbow = ["red","Yellow"]
# colors.extend(rainbow)
# print(colors)

# cars = ["Hyundai", "Tata", "Mahindra"]
# cars2 = ("Mercedes", "Volkswagen", "BMW")
# cars.extend(cars2)
# print(cars)


# cars = ["Hyundai", "Tata", "Mahindra"]
# cars2 = {"Mercedes", "Volkswagen", "BMW"}
# cars.extend(cars2)
# print(cars)



# students = ["Sakshi", "Aaditya", "Ritika"]
# students2 = {"Yash":18, "Devika":19, "Soham":19}    #only add keys, does not add values
# students.extend(students2)
# print(students)

# colors = ["voilet", "indigo", "blue"]
# rainbow = ["red","Yellow"]
# print(colors+ranbow)


# colors = ["voilet", "indigo", "blue","red","Yellow"]
# colors.pop()
# print(colors)
# colors.pop(2)
# print(colors)
# colors.remove("indigo")
# print(colors)
# del colors[3]
# print(colors)
# del colors
# print(colors)#it give error because colors is deleted
# colors.clear()
# print(colors)

# names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
# names[3] = "bablu"
# print(names)
# names[1:4] = ["bablu","nitish","abhisekh"]
# print(names)
# names[1:4] = ["bablu","nitish","abhisekh","rahul","pawan"]
# print(names)

# names = ["Harry", "Sara", "Nadia", "Oleg", "Steve"]
# nameWith_a = [item for item in names if "a" in item]
# print(nameWith_a)
# nameWith = [item for item in names if len(item)>4]
# print(nameWith)


# colors = ["voilet", "indigo", "blue", "green"]
# colors.sort()
# print(colors)

# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.sort()
# print(num)
# num.sort(reverse=True)
# print(num)


# colors = ["voilet","green", "indigo", "blue", "green"]
# colors.reverse()
# print(colors)

# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.reverse()
# print(num)

# print(colors.index("indigo"))
# print(num.index(3))

# print(colors.count("green"))
# print(num.count(2))

# newColor = colors.copy()
# print(newColor)