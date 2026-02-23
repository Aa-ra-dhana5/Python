#globals() function helps to take value of variable  of global
# when we want to use the value of global variable inside the function having same variable like global

a=50 
def show():
    a= 10
    print("Local variable : " , a)
    x= globals()['a'] #which returns a live, writable dictionary of the current global namespace.
    print("Global variable : " , x)