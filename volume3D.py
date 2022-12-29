import math

def cube(side):
	volume = side **3

def cuboid(length, breadth, height):
	volume = length * breadth * height

def cone(radius, height):
	volume = 0.333 * 3.14 * (radius ** 2) * height

def cylinder(radius, height):
	volume = 3.14 * (radius ** 2) * height

def sphere(radius):
	volume = 1.333 * 3.14 * (radius ** 3)

def hemisphere(radius):
	volume = 0.6667 * 3.14 * (radius ** 3)

def tetrahedron(side):
	volume = (side ** 3) / 6 * math.sqrt(2)

def pyramid(length, width, height):
	volume = (length * width * height) / 3
