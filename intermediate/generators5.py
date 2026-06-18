mygenerator = (i for i in range(10) if i % 2 == 0)

mylist = [i for i in range(10) if i % 2 == 0]
# The difference between a generator expression and a list comprehension is that a generator expression creates an iterator that generates values on the fly, while a list comprehension creates a list in memory that contains all the values at once. This means that a generator expression can be more memory efficient when dealing with large datasets, as it does not require storing all the values in memory at once.