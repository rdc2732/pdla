#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Proximity Display of Local Aircraft: PDLA
   This program enables the associated hardware that encompasses
   the PDLA system.  It is a low resolution, portable display of
   aircraft in the area near the user.
"""

import sys
import time

"""
Things that have to happen:
    Get current GPS location
    Get current scale factor
    Respond to button pushes
    Generate bounding box
    Generate airspace cells
    Get local aircraft
    Map aircraft to cells
    Update cell display
    Update scale factor display
    Update scale factor

Assumptions:
    Cell display is an 8x8 matrix



class Rectangle:
   def __init__(self, length, breadth, unit_cost=0):
       self.length = length
       self.breadth = breadth
       self.unit_cost = unit_cost
   
   def get_perimeter(self):
       return 2 * (self.length + self.breadth)
   
   def get_area(self):
       return self.length * self.breadth
   
   def calculate_cost(self):
       area = self.get_area()
       return area * self.unit_cost
# breadth = 120 cm, length = 160 cm, 1 cm^2 = Rs 2000
r = Rectangle(160, 120, 2000)
print("Area of Rectangle: %s cm^2" % (r.get_area()))
print("Cost of rectangular field: Rs. %s " %(r.calculate_cost()))
"""


class pdla(object):
    def __init__(self, rows, columns, range):
        self.rows = rows
        self.columns = columns
        self.range = range
        self.scale_display = scaleDisplay(self.range)

    def get_scale(self):
        return self.scale_display.value()

    def update(self):
        print("updating")

class ledMatrix:
    pass

class ledCell:
    pass

class scaleDisplay(object):
    def __init__(self, range):
        self.range = range
        self.index = int(len(self.range) / 2)

    def value(self):
        return self.range[self.index]

class scaleLED:
    pass






def main():
    # create an instance of the device with an 8x8 grid.
    # it has a range with five positions weighted as shown.
    device = pdla(8, 8, [1, 2, 5, 10, 20, 50])
    while False:
        device.update()

    print(f"Scale value = {device.get_scale()}")

if __name__ == "__main__":
    # execute only if run as a script
    main()
