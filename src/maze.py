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
        win,
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
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                cell = Cell(self.__win)
                self.__cells[i].append(cell)
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        x = self.__x1 + (i * self.cell_size_x)
        y = self.__y1 + (j * self.cell_size_y)
        # cell = Cell(self.__win)
        self.__cells[i][j].draw(x, y, (x + self.cell_size_x), (y + self.cell_size_y))
        self.__animate()

    def __animate(self):
        self.__win.redraw()
        time.sleep(0.05)
