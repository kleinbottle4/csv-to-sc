class Table(list):
    def __init__(self):
        self.table = [[]]
    def __init__(self, array_2d):
        self.table = array_2d

    def count_rows(self):
        return len(self.table)

    def count_cols(self):
        max = 0
        for i in self.table:
            if len(i) > max:
                max = len(i)
        return max

    def get_dimensions(table):
        return (self.table.count_rows(), self.table.count_cols())

    def fill(self, default):
        dimensions = self.table.get_dimensions()
        for i in range(dimensions[0]):
            self.table[i].append([default] * (dimensions[1] - dimensions[0]))
