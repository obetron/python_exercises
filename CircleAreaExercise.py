"""
Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""
from math import pi

r = float(input('Input the radius of the circle : '))
area = pi * (r**2)
print('The area of circle is with radius {0} is {1}'.format(str(r), area))
