import math


def square(side):
    area = side * side


def rectangle(length, breadth):
    area = length * breadth


def triangleBaseHeight(base, height):
    area = 0.5 * (base * height)


def triangleSides(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5


def triangle2SidesAngle(side1, side2, angle):
    area = (1 / 2) * side1 * side2 * math.sin(angle)


def triangle2AnglesSide(angle1, angle2, side):
    area = (1 / 2) * side * side * math.sin(angle1) * math.sin(angle2) / math.sin(angle1 + angle2)


def circle(radius):
    area = 3.14 * (radius * radius)


def semicircle(radius):
    area = 0.5 * 3.14 * (radius * radius)


def sector(radius, angle):
    area = 3.14 * radius * radius * angle / 360


def ellipse(minor, major):
    area = 3.14 * minor * major


def trapezoid(base1, base2, height):
    area = (base1 + base2) / 2 * height


def parallelogram(base, height):
    area = base * height


def rhombus(diagonal1, diagonal2):
    area = (diagonal1 * diagonal2) / 2


def pentagon(side):
    area = (math.sqrt(5 * (5 + 2 * (math.sqrt(5)))) * side * side) / 4


def hexagon(side):
    area = ((3 * math.sqrt(3) * (side * side)) / 2)


def octagon(side):
    area = (2 * (1 + (math.sqrt(2))) * side * side)


def converter(area, input_units, output_units):
    if input_units == "cm" and output_units == "m":
        area = area / 100
        print(area)
    elif input_units == "cm" and output_units == "inch":
        area = area * 0.393701
        print(area)
    elif input_units == "cm" and output_units == "km":
        area = area / 100000
        print(area)
    elif input_units == "m" and output_units == "cm":
        area = area * 100
        print(area)
    elif input_units == "m" and output_units == "inch":
        area = area * 39.3700787402
        print(area)
    elif input_units == "m" and output_units == "km":
        area = area / 1000
        print(area)
    elif input_units == "inch" and output_units == "cm":
        area = area * 2.54
        print(area)
    elif input_units == "inch" and output_units == "m":
        area = area * 0.0254
        print(area)
    elif input_units == "inch" and output_units == "km":
        area = area / 39370
        print(area)
