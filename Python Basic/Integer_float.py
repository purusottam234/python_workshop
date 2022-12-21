# to determine the type of code 
a = type(10)
if a == int:
    print("integer")


b = type(12.5)
if b == int:
    print("integer")
elif b == float:
    print("float")
else:
    print("string")


c= int(7.9999)
print(c)


print((2+3j)/(1-5J))