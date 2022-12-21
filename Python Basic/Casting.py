'''
It's common for numbers to be experssed as strings when dealing with input
and output. Note that '5' and 5 are different types. We can easily convert between numbers and strings
using the appropriate type keywords.
'''

a= type('5')
print(a)

b= '5' + '7'
print(b)

c = int('5')
print(c)

d = int('5')+ int('8')
print(d)


# Input function in pyrhon
# input() function is a built-in function that allows user input.

# choose a  question to ask
print("what is your name?")
name = input()
print("Hello"+" " + name)


# using input() function to rate your day
# choose a question to ask
print("how would you rate your day on a scale of 1 and 10 ?")
# set a variable equal to input()
day_rating = input()
# select an approprite output
print("you feel like a "+ day_rating + " today. Thanks for letting me know")