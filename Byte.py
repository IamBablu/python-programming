n=[10,20,0,40,15]
'''this contain ony 0 to 255 number'''
x=bytes(n)
"""it can't be modefy or change"""
print("x[0]=",x[0])
for i in x:print(i)
y=bytearray(n)
"""it can be modefy or change"""
print("y[0]=",y[0])
y[0]=70
y[1]=44
'''it can't change in floating no'''
for i in y:print(i)