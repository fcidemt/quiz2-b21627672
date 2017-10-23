'''
 Problem1: Quadratic Equation Solver

 It solves quadratic equation in a form of (ax^{2} + bx + c = 0)
 The constant values (a, b, and c) are provided as the comment line arguments.

'''

# Write your code here

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

discriminant = b ** 2 - 4 * a * c
delta = (b ** 2 - 4 * a * c) ** 0.5

if discriminant > 0:
    print("There are two solutions")
    root1 = (-b + delta) / 2 * a
    root2 = (-b - delta) / 2 * a
    print('Solutions(s): ' + '{0:.2f}'.format(root1), end=" ")
    print('{0:.2f}'.format(root2))

elif discriminant == 0:
    print("There is one solution")
    root = -b / 2 * a
    print('Solution(s): ' + '{0:.2f}'.format(root))

else:
    print("The solution is not real but complex")
  
# End of the file
