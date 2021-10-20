#!/usr/bin/env python3
# Copyright (C) 2013-2014 Florian Festi
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from boxes import *
import math

class Rectangle(Boxes):
    """A simple rectangle"""

    ui_group = "Snijlab"

    def __init__(self):
        Boxes.__init__(self)
        self.addSettingsArgs(edges.FlexSettings)
        self.buildArgParser()
        self.argparser.add_argument(
            "--width", action="store", type=int, default=148,
            help="the width of the (closed) cover")
        self.argparser.add_argument(
            "--height", action="store", type=int, default=210,
            help="the height of the cover")
        self.argparser.add_argument(
            "--cornerRadius", action="store", type=float, default=0,
            help="Radius of the corners in mm")
        self.argparser.add_argument(
            "--cornerHoleDia", action="store", type=float, default=0,
            help="add holes in the corners (0 to disable)")
        self.argparser.add_argument(
            "--cornerHoleDistance", action="store", type=float, default=10,
            help="distance in x and y from corner to hole")


    def render(self):
        self.moveTo(self.cornerRadius, 0)

        # Bottom
        self.edge(self.width - 2 * self.cornerRadius)
        self.corner(90, self.cornerRadius)

        # Right
        self.edge(self.height - 2 * self.cornerRadius)
        self.corner(90, self.cornerRadius)

        # Top
        self.edge(self.width - 2 * self.cornerRadius)
        self.corner(90, self.cornerRadius)

        # Left
        self.edge(self.height - 2 * self.cornerRadius)
        self.corner(90, self.cornerRadius)

        # corner holes:
        if self.cornerHoleDia:
            # relative position is now x=radius, y=0
            x_left = self.cornerHoleDistance - self.cornerRadius
            x_right = self.width - self.cornerHoleDistance - self.cornerRadius
            y_bottom = self.cornerHoleDistance
            y_top = self.height - self.cornerHoleDistance
            self.hole(x_left, y_bottom, self.cornerHoleDia/2)
            self.hole(x_right, y_bottom, self.cornerHoleDia/2)
            self.hole(x_right, y_top, self.cornerHoleDia/2)
            self.hole(x_left, y_top, self.cornerHoleDia/2)
