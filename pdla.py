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

class ledMatrix:
    pass

class ledCell:
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


class scaleLED:
    def __init__(self, position):
        self.position = position
        self.state = False

    def __repr__(self):
        return f"{self.position}, {self.state}"

    def set_LED(self, new_value):
        self.state = new_value

    def return_state(self):
        return self.state




def main():
    # create an instance of the device with an 8x8 grid.
    # it has a range with five positions weighted as shown.
    device = pdla(8, 8, [1, 2, 5, 10, 20, 50])
    while False:
        device.update()

    print(f"Scale value = {device.get_scale()}")
    print(f"LED Display = {device.get_scale_status()}")


if __name__ == "__main__":
    # execute only if run as a script
    main()
