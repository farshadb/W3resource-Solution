import math


""" 
This app accepts the radius of a circle from the user and compute the area
"""

radius = float(input("Enter a integer number: \n"))
circle_area = math.pi * (radius ** 2)
print(f"Circle area with radius = {radius} : \n ", circle_area)

