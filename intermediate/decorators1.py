import functools

def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

def print_name():
    print("Alice")

print_name() # Output: Alice

#print_name = start_end_decorator(print_name)

@start_end_decorator
def print_name():
    print("Alice")

print_name()

@start_end_decorator
def add(a, b):
    print(a + b)

add(3, 5) # Output: Start, 8, End

print(help(add)) # Output: Help on function add in module __main__: add(a, b)
print(add.__name__) # Output: wrapper
