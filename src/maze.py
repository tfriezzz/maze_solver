import time
import random
from window import *
from cell import *


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        if seed is not None:
            maze_seed = random.seed(seed)
        self.__create_cells()

    def __create_cells(self):
        for i in range(self.__num_cols):
            self.__cells.append([])
            for j in range(self.__num_rows):
                cell = Cell(self.__win)
                self.__cells[i].append(cell)
                if self.__win is not None:
                    self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        x = self.__x1 + (i * self.cell_size_x)
        y = self.__y1 + (j * self.cell_size_y)
        self.__cells[i][j].draw(
            x, y, (x + self.cell_size_x), (y + self.cell_size_y), "black"
        )
        self.__animate()

    def __animate(self):
        if self.__win is not None:
            self.__win.redraw()
        time.sleep(0.02)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[-1][-1].has_bottom_wall = False
        self.__cells[-1][-1].is_end_cell = True
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True

        while True:
            directions = []

            if i > 0 and not self.__cells[i - 1][j].visited:  # Left
                directions.append((i - 1, j))
            if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited:  # Right
                directions.append((i + 1, j))
            if j > 0 and not self.__cells[i][j - 1].visited:  # Up
                directions.append((i, j - 1))
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:  # Down
                directions.append((i, j + 1))

            if not directions:
                self.__draw_cell(i, j)
                return

            next_i, next_j = random.choice(directions)

            if next_i == i - 1:  # Left
                self.__cells[i][j].has_left_wall = False
                self.__cells[i - 1][j].has_right_wall = False
            elif next_i == i + 1:  # Right
                self.__cells[i][j].has_right_wall = False
                self.__cells[i + 1][j].has_left_wall = False
            elif next_j == j - 1:  # Up
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j - 1].has_bottom_wall = False
            elif next_j == j + 1:  # Down
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j + 1].has_top_wall = False

            self.__draw_cell(i, j)
            self.__draw_cell(next_i, next_j)

            self.__break_walls_r(next_i, next_j)

    def __reset_cells_visited(self):
        for i in range(len(self.__cells)):
            for j in range(len(self.__cells[0])):
                self.__cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self.__animate()
        self.__cells[i][j].visited = True
        if self.__cells[i][j].is_end_cell:
            return True

        # Try Right
        if (
            i < self.__num_cols - 1
            and not self.__cells[i][j].has_right_wall
            and not self.__cells[i + 1][j].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i + 1][j])

            if self._solve_r(i + 1, j):
                return True
            self.__cells[i][j].draw_move(self.__cells[i + 1][j], True)

        # Try Down
        if (
            j < self.__num_rows - 1
            and not self.__cells[i][j].has_bottom_wall
            and not self.__cells[i][j + 1].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])

            if self._solve_r(i, j + 1):
                return True
            self.__cells[i][j].draw_move(self.__cells[i][j + 1], True)

        # Try Left
        if (
            i > 0
            and not self.__cells[i][j].has_left_wall
            and not self.__cells[i - 1][j].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            self.__cells[i][j].draw_move(self.__cells[i - 1][j], True)

        # Try Up
        if (
            j > 0
            and not self.__cells[i][j].has_top_wall
            and not self.__cells[i][j - 1].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            self.__cells[i][j].draw_move(self.__cells[i][j - 1], True)

        return False
