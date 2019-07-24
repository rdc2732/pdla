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
    def __init__(self, rows, columns, span):
        self.rows = rows
        self.columns = columns
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
    def __init__(self, latlong):
        self.lat, self.long = latlong
        self.latlong = (self.lat, self.long)
        self.initial_latlong = self.latlong
        self.last_latlong = self.latlong
        print(f"My GPS coordinates are: {self.latlong}")

    def get_conversion(self):
        earth = 24901 # Circumference of earth in miles
        degLat = earth / 360 # miles of 1 degree latitude
        milesLat = 1 / degLat # degrees of 1 mile lstitude
        degLong = earth * math.cos(self.long * 2 * math.pi/360) / 360
        milesLong = 1 / degLong
        return (milesLong, milesLat)

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
    # It will extend (4 x scale) miles in each compass direction
    # from the center.  It will then create sub-airspaces based on
    # the number of rows and columns it will be divided into.
    def __init__(self, lat, long, rows, columns, scale):
        self.lat = lat
        self.long = long
        self.rows = rows
        self.columns = columns
        self.scale = scale



"""
1) Determine how many degrees one mile latitude is (a constant)
2) Determine how many degrees one mile longitude is (a constant based on latitude)
3) Determine UL = [latitude - (Cols / 2) * Scale, longitude + (Cols / 2) * Scale ]
4) Determine LR = [latitude + (Cols / 2) * Scale, longitude - (Cols / 2) * Scale ]
5) Determine CTR for each cell in rows, cols.


"""




def main():
    # create an instance of the device with an 8x8 grid.
    # it has a range with five positions weighted as shown.
    device = pdla(8, 8, [.5, 1, 2, 5, 10])
    default_coordinates = (-111.7304790, 33.2674290)
    gps = GPSinterface(default_coordinates)

    while False:
        device.update()

    print(f"GPS Coordinates = {gps.latlong}")
    print(f"GPS location test = {gps.test_latlong()}")
    print(f"Long/Lat conversion factors = {gps.get_conversion()}")
    print(f"Scale value = {device.get_scale()}")
    print(f"LED Display = {device.get_scale_status()}")


if __name__ == "__main__":
    # execute only if run as a script
    main()
