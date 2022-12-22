'''
List comprehension offers a shorter syntax when you want to create new list 
based on the values of an existing list

Example: based on a list of fruits, you want a new list, containing only the fruits
with the letter 'a' in the name
'''


# without list comprehension
fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# with list Comprehension we can do all that with only one line of code 
fruits = ["apple","banana","cherry","kiwi","mango"]

newlist = [x for x in fruits if "a" in x]
print(newlist)


'''
syntax:
newlist = [expression for item in iterable if condition == True]
'''