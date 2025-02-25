#!/usr/bin/env python3

# Created By: Amara Tie

# Date: Febuary 18, 2025

# This code calculates area and perimeter.

def main():
    #INPUT
    length = int(input("Enter length of the rectangle (mm): "))
    width = int(input("Enter width of the rectangle (mm): "))
    #CALCULATIONS
    area = length*width
    perimeter = 2 * (length+width)
    #OUTPUT
    print("Area is {}mm^2".format(area))
    print("Perimeter is: {}cm".format(perimeter))


if __name__ == "__main__":
    main()