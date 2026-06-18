class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} or {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Alice") # Output: Call 1 of 'say_hello', Hello, Alice!
say_hello("Bob") # Output: Call 2 of 'say_hello', Hello, Bob!