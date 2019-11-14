import random
import Board
import os
import time
import arcade

arcade.run()
OPPOSITE_DIRECTIONS = {
    'south': 'north',
    'north': 'south',
    'west': 'east',
    'east': 'west'
}


class MazeGenerator(arcade.Window):
    current_path = []
    board_rows = 10
    board_columns = 10
    start_cell = None
    count = 0

    def __init__(self, rows, columns):
        super().__init__(columns*20, rows*20, "Maze Runner")
        self.board_rows = rows
        self.board_columns = columns
        self.my_board = Board.Board(self.board_rows, self.board_columns)
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        self.start_cell = self.my_board.board[0]
        self.start_cell.start = True
        self.count = 0
        self.make_maze(self.start_cell)
        arcade.run()

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        pass

    def on_draw(self):
        arcade.start_render()

    def make_maze(self, target):
        target.current = True
        target.visited = True
        if target.value == 0:
            target.set_value(self.count)
            self.count += 1
        neighbours = self.my_board.find_neighbour(target)
        if len(neighbours) > 0:
            # pick a neighbour to visit
            direction, next_cell = random.choice(list(neighbours.items()))
            opposite_direction = OPPOSITE_DIRECTIONS[direction]
            new_walls = dict()
            new_walls[direction] = False
            next_walls = dict()
            next_walls[opposite_direction] = False
            target.set_walls(new_walls)
            next_cell.set_walls(next_walls)
            self.current_path.append(target)
            target.current = False
            return self.make_maze(next_cell)
        elif len(neighbours) == 0 and len(self.current_path) > 0:
            target.current = False
            next_cell = self.current_path.pop()
            return self.make_maze(next_cell)
        else:
            return target


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
