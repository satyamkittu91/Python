import random
import secrets
import numpy as np

a = random.random()
print(a) # Output: a random float between 0.0 and 1.0

a = random.uniform(1, 10)
print(a) # Output: a random float between 1.0 and 10.0

a = random.randint(1, 10)
print(a) # Output: a random integer between 1 and 10 (inclusive)

a = random.choice(['apple', 'banana', 'cherry'])
print(a) # Output: a random element from the list

mylist = list("abcdefghijklmnopqrstuvwxyz")
a = random.choices(mylist, k=5)
print(a) # Output: a list of 5 random elements from the list
# Items can be repeated

mylist = list("abcdefghijklmnopqrstuvwxyz")
random.shuffle(mylist)
print(mylist) # Output: the list in random order

random.seed(1)
print(random.random()) # Output: 0.13436424411240122
print(random.randint(1, 10)) # Output: 2

random.seed(1)
print(random.random()) # Output: 0.13436424411240122
print(random.randint(1, 10)) # Output: 2

random.seed(2)
print(random.random()) # Output: 0.9560342718892494
print(random.randint(1, 10)) # Output: 1

a = secrets.randbelow(10)
print(a) # Output: a random integer between 0 and 9 (inclusive)

a = secrets.randbits(4)
print(a) # Output: a random integer with 4 random bits (between 0 and 15)

a = secrets.choice(['apple', 'banana', 'cherry'])
print(a) # Output: a random element from the list

a = np.random.rand(3)
print(a) # Output: an array of 3 random floats between 0.0 and 1.0

a = np.random.randint(1, 10, size=5)
print(a) # Output: an array of 5 random integers between 1 and 9 (inclusive)

a = np.random.randint(1, 10, size=(2, 3))
print(a) # Output: a 2x3 array of random integers between 1 and 9 (inclusive)

a = np.random.choice(['apple', 'banana', 'cherry'], size=5)
print(a) # Output: an array of 5 random elements from the list

a = np.random.seed(1)
print(np.random.rand()) # Output: 0.417022004702574