# How to import a library into your script
import cmath

def calculate_roots(a, b, c):
    # Returns the discriminate as an object to use in our if else statement
    discriminate = b**2 - 4*a*c
    # Here is where we will calculate the first root using
    # The cmath.sqrt function from the cmath library
    # this will need to be the plus half of the quadratic
    root_1 = 
    # this will need to be the minus half of the quadratic
    root_2 = 
    return root_1, root_2
# Test your function
print(calculate_roots(1, 1, 1))  # Should print (3.0, 2.0)