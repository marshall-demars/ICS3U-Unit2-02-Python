#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Sept 2022
# This program calculates area and perimeter of a circle with 15mm radius

import math


def main():
    # this function calculates the area and perimeter

    # input
    length_of_rectangle = int(input("Enter length of the rectangle (mm): "))
    width_of_rectangle = int(input("Enter width of the rectangle (mm): "))

    # process
    area_of_rectangle = length_of_rectangle * width_of_rectangle
    perimeter_of_rectangle = 2 * (length_of_rectangle + width_of_rectangle)

    # output
    print("\nArea is {} mm².".format(area_of_rectangle))
    print("Perimeter is {} mm.".format(perimeter_of_rectangle))

    print("\nDone.")


if __name__ == "__main__":
    main()
