#itertools : product, permutations, combinations, combinations_with_replacement, count, cycle, repeat, accumulate, groupby, islice, starmap, tee, zip_longest
from itertools import product
from itertools import permutations, combinations, combinations_with_replacement
from itertools import accumulate
from itertools import groupby
from itertools import count, cycle, repeat

#product
a = [1, 2, 3]
b = ['a', 'b', 'c']
prod = product(a, b) # Cartesian product of a and b
print(list(prod))

#permutations, combinations, combinations_with_replacement
a = [1, 2, 3]
perm = permutations(a) # All possible permutations of a
print(list(perm))

a = [1, 2, 3]
comb = combinations(a, 2) # All possible combinations of a with length 2
print(list(comb))
comb_wr = combinations_with_replacement(a, 2) # All possible combinations of a with length 2, allowing for repeated elements
print(list(comb_wr))

#accumulate
a = [1, 2, 3, 4]
acc = accumulate(a) # Cumulative sum of a
print(list(acc))
a = [1, 2, 5, 3, 4]
acc_max = accumulate(a, func=max) # Cumulative maximum of a
print(list(acc_max))

# groupby

def smaller_than_3(x):
    return x < 3

a = [1, 1, 2, 2, 3, 3, 4, 5]
grouped = groupby(a, key=smaller_than_3) # Group consecutive elements in a
for key, group in grouped:
    print(key, list(group))

persons = [{'name': 'Alice', 'age': 30},
           {'name': 'Bob', 'age': 25},
            {'name': 'Charlie', 'age': 30},
            {'name': 'David', 'age': 25}]

grouped = groupby(persons, key=lambda x: x['age']) # Group consecutive elements in persons by age
for key, group in grouped:
    print(key, list(group))

# To group all persons by age (not just consecutive equal ages), sort first:
persons_sorted = sorted(persons, key=lambda x: x['age'])
grouped = groupby(persons_sorted, key=lambda x: x['age'])
for key, group in grouped:
    print(key, list(group))


# Count
for i in count(10): # start from 10 to infinity
    print(i)
    if i == 20:
        break


# Cycle
a = [1, 2, 3]
for i in cycle(a): # Cycle through a indefinitely
    print(i)
    if i == 3:
        break

# Repeat
for i in repeat(10, 5): # Repeat 10 for 5 times
    print(i)