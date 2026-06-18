# Lambda functions are anonymous functions defined using the lambda keyword. They can take any number of arguments but can only have one expression. The syntax is: lambda arguments: expression.   
# lambda arguments: expression
from functools import reduce
add10 = lambda x: x + 10
print(add10(5)) # Output: 15

def add10(x):
    return x + 10

print(add10(5)) # Output: 15

points2d = [(1, 2), (15, 1), (5, -1), (10, 4)]
def sort_by_y(x):
    return x[1]

points2d_sorted = sorted(points2d, key=sort_by_y)
print(points2d_sorted) # Output: [(5, -1), (15, 1), (1, 2), (10, 4)]

sorted_points2d = sorted(points2d, key=lambda x: x[1])
print(sorted_points2d) # Output: [(5, -1), (15, 1), (1, 2), (10, 4)]


a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a) # Map applies the lambda function to each element of the iterable a
print(list(b)) # Output: [2, 4, 6, 8, 10]

#list comprehension way
c = [x*2 for x in a]
print(c) # Output: [2, 4, 6, 8, 10]

a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x%2 == 0, a) # Filter applies the lambda function to each element of the iterable a and returns only those elements for which the function returns True
print(list(b)) # Output: [2, 4, 6]

# list comprehension way
c = [x for x in a if x%2 == 0]
print(c) # Output: [2, 4, 6]


# reduce
a = [1, 2, 3, 4, 5]
b = reduce(lambda x, y: x + y, a) # Reduce applies the lambda function cumulatively to the items of the iterable a, from left to right, so as to reduce the iterable to a single value

