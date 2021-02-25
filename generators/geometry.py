# 20/02/2021
# For now only focus on basic shape -- 2D
# Square, rectangle, circle, and triangle.

# 24/02/2021
# Make a clean code.
# - Make it simple, stupid!
# - Meaningful variables name
# - Improve code until it's not necessary to write a obvious and redundant comments
# - Let one function do merely one task

# 25/02/2021
# Do tasks from yesterday


import math
import random

# Math stuffs
PI = math.pi
SQRT = math.sqrt

DEG_TO_RAD = math.radians
RAD_TO_DEG = math.degrees

SIN = math.sin


# Basic shapes #
class Square():
	def area(side):
		return side * side
		
	def side(area):
		return SQRT(area)
		
	def diagonal(side):
		return SQRT(2) * side
		
	def perimeter(side):
		return 4 * side


class Rectangle():		
	def area(length, width):
		return length * width
		
	def length(area, width):
		return area / width
		
	def width(area, length):
		return area / length
		
	def diagonal(length, width):
		return SQRT((width**2) + (length**2))
		
	def perimeter(length, width):
		return 2 * (length + width)


class Circle():
	def area(radius):
		return PI * (radius**2)
		
	def radius(area):
		return SQRT(area / PI)

	def diameter(radius):
		return 2 * radius
		
	def circumference(radius):
		return 2 * pi * radius


class Triangle():
	def area(base, height):
		return (base * height) / 2
		
	def height(area, base):
		return 2 * (area / base)
		
	def base(area, height):
		return 2 * (area / height)
		
	def side_a(area, base, gamma):
		gamma = DEG_TO_RAD(gamma)
		return 2 * (area / (base * SIN(gamma)))
				
	def side_c(perimeter, side, base):
		return perimeter - side - base
	
	def perimeter(side_a, base, side_c):
		return side_a + base + side_c
