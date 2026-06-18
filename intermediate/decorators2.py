import functools

def repeat(num_times): #argument for the decorator
    def decorator_repeat(func): #the actual decorator function
        @functools.wraps(func) #preserves the original function's metadata
        def wrapper(*args, **kwargs): #the wrapper function that will replace the original function
            for _ in range(num_times): #repeat the function num_times
                result = func(*args, **kwargs) #call the original function and store the result
            return result #return the result of the last call to the original function
        return wrapper #return the wrapper function
    return decorator_repeat #return the actual decorator function


@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")


greet("Alice") # Output: Hello, Alice! (printed 3 times)