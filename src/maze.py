import time
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
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
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
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)
