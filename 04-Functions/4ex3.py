###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
def triangle_area(a,b,c):
    s = (a + b + c)/2
    result = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return result

print(f'The area of ​​a triangle with sides 2 6 7 is {triangle_area(2,6,7)}')
#print('The area of ​​a triangle with sides ... is ...')
#print('The area of ​​a triangle with sides ... is ...')