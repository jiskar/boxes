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
        self.argparser.add_argument("--rotated", action="store", type=boolarg, default=False)


    def render(self):
        self.moveTo(self.radius, 0)

        hinge_width = 30

        # prevent corner radius from getting too big:
        self.radius = min(self.radius, self.width, self.height / 2)

        if self.rotated:
            # Booklet is generated 90 degrees rotated to align woodfibers with flex
            # Right of booklet, bottom in drawing
            self.edge(self.height - 2 * self.radius)
            self.corner(90, self.radius)

            # Top of booklet, right in drawing
            self.edge(self.width - self.radius)
            self.edges["X"](hinge_width, self.height)  # hinge
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
            self.edges["X"](hinge_width, self.height)  # hinge
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


