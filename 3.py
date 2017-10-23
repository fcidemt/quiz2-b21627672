'''
 Problem3: Set Operations

 This program finds the intersection and union and difference of two sets
 (A and B) each of which corresponds to different command line argument and
 the elements of A and B should be separated by commas.

'''


# Write your code here

import sys

setA = sys.argv[1].split(",")
setB = sys.argv[2].split(",")
intersection = []
differenceA_B = []
differenceB_A = []

for i in setA:
    if i in setB:
        intersection.append(i)
    else:
        differenceA_B.append(i)

for j in setB:
    if j not in setA:
        differenceB_A.append(j)

union = setA + differenceB_A

print('Set A:', setA)
print('Set B:', setB)
print('Intersection of A and B:', intersection)
print('Union of A and B:', union)
print('Difference of A and B:', differenceA_B)



# End of the file
