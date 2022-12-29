import math


def cube(side):
	area = 6 * side * side

def cuboid(length, breadth, height):
	area = 2 * (length * breadth + breadth * height + length * height)

def cone(radius, height):
	area = 3.14 * radius(radius + math.sqrt((height * height) + (radius * radius))

def cylinder(radius, height):
	area = 2 * 3.14 * radius * height + 2 * 3.14 * (radius * radius)

def sphere(radius):
	area = 4 * 3.14 * radius * radius

def hemisphere(radius):
	area = 2 * 3.14 * radius * radius

def tetrahedron(side):
	area = math.sqrt(3) * side * side
