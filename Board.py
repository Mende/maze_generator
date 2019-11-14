import Cell


class Board():
    board = []
    max_rows = 0
    max_columns = 0

    def __str__(self):
        new_str = ''
        for row in range(self.max_rows):
            for col in range(self.max_columns):
                new_str += str(self.board[col + row * self.max_columns])
            new_str += "\n"
        return new_str

    def __init__(self, max_rows, max_columns):
        self.max_rows = max_rows
        self.max_columns = max_columns
        # make board
        for row in range(max_rows):
            for col in range(max_columns):
                self.board.append(Cell.Cell(row, col))

    def find_neighbour(self, target):
        neighbours = dict()
        # north
        if target.row + 1 < self.max_rows:
            index = (target.row + 1)*self.max_columns + target.column
            if not(self.board[index].visited):
                neighbours['north'] = self.board[index]

        # east
        if target.column + 1 < self.max_columns:
            index = (target.row * self.max_columns + (target.column + 1))
            if not(self.board[index].visited):
                neighbours['east'] = self.board[index]

        # south
        if target.row - 1 >= 0:
            index = ((target.row - 1)*self.max_columns + target.column)
            if not(self.board[index].visited):
                neighbours['south'] = self.board[index]

        # west
        if target.column - 1 >= 0:
            index = (target.row * self.max_columns + (target.column - 1))
            if not(self.board[index].visited):
                neighbours['west'] = self.board[index]

        return neighbours
