# import gc

# print(gc.get_threshold())

import gc

class A:
    def __init__(self):
        print("A created")

    def __del__(self):
        print("A destroyed")

class B:
    def __init__(self):
        print("B created")

    def __del__(self):
        print("B destroyed")


a = A()
b = B()

a.ref = b
b.ref = a

del a
del b

gc.collect()
print(gc.garbage)