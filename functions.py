import math

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
