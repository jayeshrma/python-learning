from functools import wraps

def myDecorator(func):
    @wraps(func) # Perserve metadata
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    
    return wrapper

@myDecorator
def greet():
    print("Hello, I am being decorated")
    
greet()
print(greet.__name__) # prints wrapper if metadata not preserved