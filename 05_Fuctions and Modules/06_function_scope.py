def sum(a, b):
    # a and b are local variables i.e, we can't access them outside the function...
    c = a + b
    print(z) # it creates a local variable called z which is destroyed after this function is returns.
    return c

def greet():
    z = 32 # Local variable
    print("Hello")

z = 8 # z is a global variable i.e, we can access it anywhere...
print(z)
print(sum(4, 6))
print(z)

