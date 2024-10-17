# tup = (1,2,3,4)
# tup2 = ("Bablu", 4, "Nitish", "Rahul")
# print(tup)
# print(tup2)
# print(tup[2])
# print(tup[-3])
# print(tup2[1:3])


# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[1:8:2])
# if "mouse" in animals:
#     print("mouse present")
# else:
#     print("mouse not present")


# countries = ("Spain", "Italy", "India", "England", "Germany")
# l1 = list(countries)
# l1.append("Russia")
# l1.pop(2)
# l1[2] = "Finland"
# countries = tuple(l1)
# print(countries)

# countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
# countries2 = ("Vietnam", "India", "China")
# southEastAsia = countries+countries2
# print(southEastAsia)


# info = ("Marcus", 20, "MIT")
# (name, age, university) = info
# print("Name:", name)
# print("Age:",age)
# print("Studies at:",university)


# fauna = ("cat", "dog", "horse", "pig", "parrot", "salmon")
# (*animals, bird, fish) = fauna
# print("Animals:", animals)
# print("Bird:", bird)
# print("Fish:", fish)

fauna = ("parrot", "cat", "dog", "horse", "pig", "salmon")
(bird, *animals, fish) = fauna
print("Animals:", animals)
print("Bird:", bird)
print("Fish:", fish)