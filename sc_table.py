
#sc_table.py contains the SC_table class used in csv_to_sc.py

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

from parse_strings import num_to_sc_col

class SC_table():
    def __init__(self):
        self.array = [[]]

    def __init__(self, array_2d):
        self.array = array_2d

    def get_max_height(self):
        return len(self.array)

    def get_max_width(self):
        widths = [len(i) for i in self.array]
        if len(widths) == 0:
            return 0
        else:
            return max(widths)

    def get_col_widths(self):
        widths = [10 for i in range(self.get_max_width())]
        for row in self.array:
            for i, cell_string in enumerate(row):
                cell_width = len(cell_string)
                if cell_width > widths[i]:
                    widths[i] = cell_width
        return widths

    def get_cell_formats(self):
        widths = self.get_col_widths()
        formats = []
        for i, width in enumerate(widths):
            col_i = num_to_sc_col(i)
            message = "format {0} {1} 2 0".format(col_i, width)
            formats.append(message)
        return formats
