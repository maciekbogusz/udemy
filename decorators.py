import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_fun():
        print("in the decorator!")
        func()
        print("after decorator")
    return function_that_runs_fun

@my_decorator
def my_function():
    print("I`m the function")

#my_function()
####

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("I`m decorator")
            if number == 56:
                print("Not running the function")
            else: 
                print("Running the function")
                func(*args, **kwargs)
            print("After decorator")          
        return function_that_runs_func
    return my_decorator

@decorator_with_arguments(2)
def my_function_two(x, y):
    print(x+y)

my_function_two(57,67)