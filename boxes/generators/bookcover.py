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

class BookCover(Boxes):
    """Folding wood booklet"""

    ui_group = "Snijlab"

    def __init__(self):
        Boxes.__init__(self)
        self.addSettingsArgs(edges.FlexSettings)
        self.buildArgParser()
        self.argparser.add_argument(
            "--width", action="store", type=int, default=102,
            help="the width of the (closed) cover")
        self.argparser.add_argument(
            "--height", action="store", type=int, default=144,
            help="the height of the cover")
        self.argparser.add_argument(
            "--radius", action="store", type=float, default=10,
            help="Radius of the corners in mm")
        self.argparser.add_argument(
            "--thickness_when_closed", action="store", type=float, default=19,
            help="Thickness of the closed cover (approximately)")
        self.argparser.add_argument(
            "--density", action="store", type=float, default=670,
            help="Density of the material in kg/m³")
        self.argparser.add_argument(
            "--torque_factor", action="store", type=float, default=4,
            help="ratio of sninge torque to cover torque")
        self.argparser.add_argument("--rotated", action="store", type=boolarg, default=False)


    def render(self):
        self.moveTo(self.radius, 0)

        # calculate the torque that the cover applies on the sninge when lying flat:
        cover_weight = self.density * self.width * self.height * self.thickness * 1e-9  # in kg
        cover_torque = 0.5 * self.width * cover_weight * 9.81
        sninge_torque = self.torque_factor * cover_torque

        # calculate hinge_width from thickness when closed (assuming it will form like a half circle)
        hinge_width = math.pi * ( self.thickness_when_closed / 2 )

        # prevent corner radius from getting too big:
        self.radius = min(self.radius, self.width, self.height / 2)

        if self.rotated:
            # Booklet is generated 90 degrees rotated to align woodfibers with flex
            # Right of booklet, bottom in drawing
            self.edge(self.height - 2 * self.radius)
            self.corner(90, self.radius)

            # Top of booklet, right in drawing
            self.edge(self.width - self.radius)
            self.edges["X"](hinge_width, self.height, torque=sninge_torque)  # hinge
            self.edge(self.width - self.radius)
            self.corner(90, self.radius)

            # Left of booklet, top in drawing
            self.edge(self.height - 2 * self.radius)

            self.corner(90, self.radius)

            # Bottom of booklet, left in drawing
            self.edge(self.width - self.radius)
            self.edge(hinge_width)
            self.edge(self.width - self.radius)

            self.corner(90, self.radius)

        else:
            # Bottom of booklet
            self.edge(self.width - self.radius)
            self.edges["X"](hinge_width, self.height, torque=sninge_torque)  # hinge
            self.edge(self.width - self.radius)
            self.corner(90, self.radius)

            # Right of booklet, bottom in drawing
            self.edge(self.height - 2 * self.radius)
            self.corner(90, self.radius)

            # Top of booklet, right in drawing
            self.edge(self.width - self.radius)
            self.edge(hinge_width)
            self.edge(self.width - self.radius)
            self.corner(90, self.radius)

            # Left of booklet, top in drawing
            self.edge(self.height - 2 * self.radius)
            self.corner(90, self.radius)


