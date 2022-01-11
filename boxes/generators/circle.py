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

class Circle(Boxes):
    """A circle or ring"""

    ui_group = "Snijlab"

    def __init__(self):
        Boxes.__init__(self)
        self.buildArgParser()
        self.argparser.add_argument(
            "--outer_diameter", action="store", type=float, default=100,
            help="Outer diameter")
        self.argparser.add_argument(
            "--inner_diameter", action="store", type=float, default=70,
            help="inner diameter (0 for closed)")
        self.argparser.add_argument(
            "--edge_holes", action="store", type=int, default=7,
            help="number of holes around the edge")
        self.argparser.add_argument(
            "--edge_hole_diameter", action="store", type=float, default=3,
            help="diameter of edge holes")
        self.argparser.add_argument(
            "--edge_hole_distance", action="store", type=float, default=7.5,
            help="distance of holes to edge")


    def render(self):
        self.moveTo(0, 0)
        x = 0
        y = 0
        self.circle(x, y, self.outer_diameter / 2)
        self.circle(x, y, self.inner_diameter / 2)

        if self.edge_holes > 0:
            angle = (2*math.pi) / self.edge_holes
            radius = self.outer_diameter/2 - self.edge_hole_distance
            for i in range(0,self.edge_holes):

                hole_x = radius * math.sin(i*angle)
                hole_y = radius * math.cos(i*angle)
                self.circle(hole_x, hole_y, self.edge_hole_diameter / 2)
