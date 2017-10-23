'''
 Problem2: Even Number Evaluator

 It consider only even numbers (E) within a list of numbers (L). 
 
 The numbers in the list should be; 
 a) greater than zero, 
 b) provided in command line arguments and, 
 c) separated by commas.

 Note: This program discards negative values

'''

# Write your code here

import sys

L = sys.argv[1].split(",")
E = []

for i in L:
    i = int(i)
    if i > 0 and i % 2 == 0:
        E.append(int(i))
    else:
        pass

total = 0
for i in L:
    i = int(i)
    if i > 0:
        total = total + i
    else:
        pass

print('Even Numbers:', E)
print('Sum of Even Numbers:', sum(E))
print('Even Number Rate: ' + '{0:.3f}'.format(sum(E) / total))


# End of the file
