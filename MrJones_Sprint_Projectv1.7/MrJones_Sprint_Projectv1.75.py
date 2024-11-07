# How to import a library into your script
import cmath
def calculate_roots(a, b, c):
    # Returns the discriminate as an object to use in our if else statement
    discriminate = (b**2 - 4*a*c)
    # Here is where we will calculate the first root using The cmath.sqrt function from the cmath library 
    root_1 = (-b + cmath.sqrt(discriminate)) / (2*a)
    # this will need to be the minus half of the quadratic
    root_2 = (-b - cmath.sqrt(discriminate)) / (2*a)
# Test your function
    if discriminate > 0:
        print(f'There are two roots: {root_1} and {root_2}')
    elif discriminate == 0:
        print(f'There is one real root at {root_1}')
    else:
        return root_1, root_2
print(calculate_roots(1, 1, 1))  # Should print (3.0, 2.0)