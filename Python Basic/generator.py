'''
In Python, a generator is a function that returns an iterator that produces a sequence of values when iterated over.

Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once.

'''

def my_generator(n):
    # initialize counter
    value = 0
    # loop until counter is less than n
    while value < n:
        # produce the current value of the counter
        yield value
        # increment the counter
        value +=1

# iterator over the generator object produced by my_generator
for value in my_generator(3):
    # print each value produced by generator
    print(value)



'''
Advantages of Generators Over Other Iterators
Generators have some advantages over other iterators in Python:

They are easy to implement and can be more memory-efficient than storing an entire sequence in memory.
They can be used to produce an "infinite" sequence of values, by using a while True loop and yielding values indefinitely.
They can be combined with other iterators using the itertools module to produce complex sequences of values.

'''