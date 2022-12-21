'''
When writing strings, you may want to include variables in the output. String
interpolation includes the variable names as placeholders within the string
There are two standards methods for achieving string interpolation
comma seperators and format
'''


# comma separators
# Variables may be interpolated into string using commas to seperate clauses. It's similar
#  to the + operator, except it adds spacing for you
games = "football"
print("Games you like most",games)


# format :

owner = "Harry harry"
age = 100

print("the founder of city store,{}, is now {} years old".format(owner,age))


# len() function
# the len() function determines the number of characters in the given string

a= len("helloworld")
print(a)

# lower () function

name = "Purusottam"

print(name.lower())

# capitalize() function
print(name.capitalize())

# upper() function

print(name.upper())


# count() function
# It count the number of instance in the word
print(name.count("u"))
