#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Proximity Display of Local Aircraft: PDLA
   This program enables the associated hardware that encompasses
   the PDLA system.  It is a low resolution, portable display of
   aircraft in the area near the user.
"""

import sys
import time
import math

"""
Things that have to happen:
x    Get current GPS location
x    Get current scale factor
    Generate bounding box
    Generate airspace cells
    Get local aircraft
    Map aircraft to cells
    Update cell display
    Update scale factor display
    Update scale factor
    Respond to button pushes

Assumptions:
    Cell display is an 8x8 matrix




"""


class pdla(object):
    def __init__(self, grid, span):
        self.rows, self.columns = grid
        self.span = span
        self.scale_display = scaleDisplay(self.span)

    def get_scale(self):
        return self.scale_display.value()

    def get_scale_status(self):
        return self.scale_display.ledStatus()

    def update(self):
        print("updating")

class ledMatrix(object):
    pass

class ledCell(object):
    pass

class scaleDisplay(object):
    def __init__(self, markers):
        self.markers = markers
        self.span = len(self.markers)
        self.index = int(self.span / 2)
        self.LEDs = []
        for self.LED in range(self.span):
            self.LEDs.append(scaleLED(self.LED))
        self.LEDs[self.index].set_LED(True)

    def value(self):
        return self.markers[self.index]

    def ledStatus(self):
        self.statuses = []
        for self.LED in self.LEDs:
            self.statuses.append(self.LED.return_state())
        return self.statuses

class scaleLED(object):
    def __init__(self, position):
        self.position = position
        self.state = False

    def __repr__(self):
        return f"{self.position}, {self.state}"

    def set_LED(self, new_value):
        self.state = new_value

    def return_state(self):
        return self.state

class GPSinterface(object):
    def __init__(self, longlat):
        self.long, self.lat  = longlat
        self.longlat = (self.long, self.lat)
        self.initial_longlat = self.longlat
        self.last_longlat = self.longlat

    def get_conversion(self):
        earth = 24901 # Circumference of earth in miles
        degreesPerMileLat = 360 / earth # degrees of 1 mile lstitude
        milesPerDegreeLong = earth * math.cos(self.lat * 2 * math.pi/360) / 360
        degreesPerMileLong = 1 / milesPerDegreeLong
        return (degreesPerMileLong, degreesPerMileLat)

    # Update the system gps coordinates with new coordinates
    def update_latlong(self):
        pass

    # Utilize the gps interface to read new coordinates
    def get_new_latlong(self):
        pass

    # Account for minor variations and set true only if actual
    # gps coordinates are x% differnt from current system gps
    def test_latlong(self):
        return False

class airSpace(object):
    # The airspace is going to be created from the center lat, long.
    # It will extend (rows/2 or cols/2 x scale) miles in each compass direction
    # from the center.  It will then create sub-airspaces based on
    # the number of rows and columns it will be divided into.
    def __init__(self, longlat, grid, scale, degreeConversions):
        self.long, self.lat = longlat
        self.rows, self.columns = grid
        self.scale = scale
        self.longDegConv, self.latDegConv = degreeConversions
        self.degreeConversions = (self.longDegConv, self.latDegConv)
        self.UL = (self.long - self.scale * self.columns * self.longDegConv, \
                   self.lat + self.scale * self.rows * self.latDegConv)
        self.LR = (self.long + self.scale * self.columns * self.longDegConv, \
                   self.lat - self.scale * self.rows * self.latDegConv)
        print(f"{(self.long, self.lat)}")

        self.latOffset = self.scale * self.latDegConv
        self.longOffset = self.scale * self.longDegConv

        # preset the initial cellCoord to be 1/2 a box above and left of UL. When it is incremented
        # by a full offset it will end up in the correct boxes for each row and column
        self.cellCoord = (self.UL[0] - self.longOffset / 2, self.UL[1] - self.latOffset / 2)

        # build an empty 2D array
        self.arr = [[None for i in range(self.columns)] for j in range(self.rows)]

        for self.i in range(self.rows):
            for self.j in range(self.columns):
                self.newLong = self.cellCoord[0] + self.longOffset * self.i
                self.newLat = self.cellCoord[1] + self.latOffset * self.j
                self.arr[self.i][self.j] = \
                    airSpace((self.newLong, self.newLat),(0,0), self.scale, self.degreeConversions)




def main():
    # create an instance of the device with an 8x8 grid.
    # it has a range with five positions weighted as shown.
    gridsize = (8,8) # rows, columns
    device = pdla(gridsize, [.5, 1, 4, 50, 100])
    currentScale = device.get_scale()
    default_coordinates = (-111.7304790, 33.2674290)
    gps = GPSinterface(default_coordinates)
    currentGPS = gps.longlat
    degreeConversions = gps.get_conversion()
    airspace = airSpace(currentGPS, gridsize, currentScale, degreeConversions)

    while False:
        device.update()

    # print(f"GPS Coordinates = {currentGPS}")
    # print(f"GPS location test = {gps.test_latlong()}")
    # print(f"Long/Lat conversion factors = {degreeConversions}")
    # print(f"Scale value = {currentScale}")
    # print(f"LED Display = {device.get_scale_status()}")


if __name__ == "__main__":
    # execute only if run as a script
    main()
