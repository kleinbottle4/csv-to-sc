#table.py contains the Table class used in csv_to_sc.py
#
#Copyright (C) 2019  syed343 (GitHub)
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see https://www.gnu.org/licenses/
#or https://github.com/syed343/csv-to-sc/blob/master/LICENSE/.

class Table(list):
    def __init__(self):
        self.table = [[]]

    def __init__(self, array_2d):
        self.table = array_2d

    def get_height(self):
        return len(self.table)

    def get_width(self):
        widths = [len(i) for i in self.table]
        if len(widths) == 0:
            return 0
        else:
            return max(widths)

    def get_dimensions(table):
        return (self.table.count_rows(), self.table.count_cols())

    def fill(self, default):
        dimensions = self.table.get_dimensions()
        for i in range(dimensions[0]):
            self.table[i].append([default] * (dimensions[1] - dimensions[0]))
