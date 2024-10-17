s1={1,2,"a","b",True}
print(type(s1))
print(s1)
s1.add("hello")
print(s1)
s1.update([10,20,30])
print(s1)
s1.remove("b")
print(s1)


s2={1,2,3,4,5}
print(s2)
s3={3,4,5,6,7}
print(s3)
print(s2.intersection(s3))
print(s2.union(s3))