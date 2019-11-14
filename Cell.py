import chalk

class Cell():
    row = 0
    column = 0
    start = False
    visited = False
    value = 0
    current = False
    walls = {
        'north':  True,
        'east':   True,
        'south':  True,
        'west':   True
    }

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.visited = False

    def __str__(self):
        cell = "[{0:03d}] ".format(self.value)
        if self.start:
            return chalk.green(cell)
        elif self.current:
            return chalk.red(cell)
        elif self.visited:
            return chalk.yellow(cell)
        return cell

    def set_current(self, value):
        self.current = value

    def set_value(self, value):
        self.value = value

    def set_walls(self, walls):
        self.walls.update(walls)

    def get_coordinates(self):
        return [self.row, self.column]
