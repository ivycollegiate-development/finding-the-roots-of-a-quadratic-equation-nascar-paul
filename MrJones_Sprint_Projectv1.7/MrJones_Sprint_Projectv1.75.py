# How to import a library into your script
import math
def calculate_roots(a, b, c):
    # Returns the discriminate as an object to use in our if else statement
    discriminate = (b**2 - 4*a*c) ** 0.5
    # Here is where we will calculate the first root using
    # The cmath.sqrt function from the cmath library
    # this will need to be the plus half of the quadratic
    root_1 = float((-b + discriminate) / (2*a))
    # this will need to be the minus half of the quadratic
    root_2 = float((-b - discriminate) / (2*a))
    return root_1, root_2
# Test your function
if discriminate > 0:
    print(f'There are two roots: {root_1} and {root_2}')
elif discriminate == 0:
    print(f'There is one real root at {root_1}')
else:
    return None

print(calculate_roots(1, 1, 1))  # Should print (3.0, 2.0)