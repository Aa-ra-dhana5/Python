# Debugging Function Calls
#Create a decorator to print the fiunction name and the values its arguments every time the function is called.

def name_func(func):
    def print_name(*args , **kwargs):
        arg_val = ', '.join(str(arg) for arg in args)
        kwargs_val = ', '.join(str(kwarg) for kwarg in kwargs.items())
        
        print(f"Calling {func.__name__} with args {arg_val}")
        return func(*args, **kwargs)
    return print_name

@name_func

def example(n):
    pass    

example(2)