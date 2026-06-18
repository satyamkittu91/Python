import sys
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

print(firstn(5)) # Output: [0, 1, 2, 3, 4]

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sys.getsizeof(firstn(100000))) # Output: 900000, the list created by firstn() takes up a lot of memory because it stores all the values in memory at once.
print(sys.getsizeof(firstn_generator(100000))) # Output: 112, the generator object itself takes up some memory, but it does not store all the values in memory at once.