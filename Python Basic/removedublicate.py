'''
Remove dublicate in list

Create a dictionary, using the List items as keys. This will automatically remove any 
duplicates because dictionaries cannot have duplicate keys.
'''

mylist = ["a","b","c","a"]
mylist = list(dict.fromkeys(mylist))
print(mylist)