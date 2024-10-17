# info = {"Carla", 19, False, 5.9, 19}
# print(info)
# for item in info:
#     print(item)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.add("Helsinki")
# print(cities)
# cities2 = ["Ranchi", "Delhi","Patna","London"]
# cities.update(cities2)
# print(cities)
# cities.remove("Delhi")
# print(cities)
# cities.discard("Patna")
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# item = cities.pop()
# print(cities)
# print(item)
# del cities
# print(cities)
# cities.clear()
# print(cities)
# if "Tokyo" in cities:
#     print("present")
# else:
#     print("not")

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.union(cities2)
# print(cities3)
# cities.update(cities2)
# print(cities)
# cities3 = cities.intersection(cities2)
# print(cities3)
# cities2.intersection_update(cities)
# print(cities2)


# cities3 = cities.symmetric_difference(cities2)
# print(cities3)
# cities2.symmetric_difference_update(cities)
# print(cities2)


# cities3 = cities.difference(cities2)
# print(cities3)
# cities2.difference_update(cities)
# print(cities2)


# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.isdisjoint(cities2))
# cities2 = {"Seoul", "Kabul"}
# print(cities.isdisjoint(cities2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.issuperset(cities2))
cities2 = {"Tokyo", "Madrid"}
print(cities.issuperset(cities2))
print(cities.issubset(cities2))
print(cities2.issubset(cities))
