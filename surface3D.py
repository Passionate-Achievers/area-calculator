import math


def cube(side):
	area = 6 * side ** 2
	

def cuboid(length, breadth, height):
	area = 2 * (length * breadth + breadth * height + length * height)
	

def cone(radius, height):
	area = 3.14 * radius(radius + math.sqrt((height ** 2) + (radius ** 2))
			     

def cylinder(radius, height):
	area = 2 * 3.14 * radius * height + 2 * 3.14 * (radius ** 2)
			     

def sphere(radius):
	area = 4 * 3.14 * (radius ** 2)
			     

def hemisphere(radius):
	area = 2 * 3.14 * (radius **2)
			     

def tetrahedron(side):
	area = math.sqrt(3) * (side ** 2)
			     

def pyramid(length, width, heigth):
	area = length * width + length * math.sqrt((width/2)**2 + height**2) + width * math.sqrt((length/2)**2 + height ** 2)
