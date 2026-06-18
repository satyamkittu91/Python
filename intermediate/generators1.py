def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()

'''
for i in g:
    print(i) # Output: 1, then 2, then 3
'''
    
'''    
value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)
'''

print(sorted(g)) # Output: [1, 2, 3] even though the generator has been exhausted, sorted() can still iterate over it and return the sorted list of values.