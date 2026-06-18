def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1


cd = countdown(5)
value = next(cd)
print(value) # Output: 5

value = next(cd)
print(value) # Output: 4

print(next(cd)) # Output: 3
print(next(cd)) # Output: 2
print(next(cd)) # Output: 1

print(next(cd)) # Output: StopIteration exception, since the generator is exhausted