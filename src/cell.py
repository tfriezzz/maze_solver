from window import *
# from maze import *


class Cell:
    def __init__(self, window_instance):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window_instance

    def draw(self, x1, y1, x2, y2, cell_color="black"):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        center_x = (self.__x1 + self.__x2) / 2
        center_y = (self.__y1 + self.__y2) / 2
        self.__center = Point(center_x, center_y)

        cell_color = cell_color

        top_left = Point(x1, y1)
        top_right = Point(x2, y1)
        bottom_left = Point(x1, y2)
        bottom_right = Point(x2, y2)

        if self.has_left_wall:
            line = Line(top_left, bottom_left)
            self.__win.draw_line(line, cell_color)
        if self.has_right_wall:
            line = Line(top_right, bottom_right)
            self.__win.draw_line(line, cell_color)
        if self.has_top_wall:
            line = Line(top_left, top_right)
            self.__win.draw_line(line, cell_color)
        if self.has_bottom_wall:
            line = Line(bottom_left, bottom_right)
            self.__win.draw_line(line, cell_color)

    def draw_move(self, to_cell, undo=False):
        if not undo:
            red_line = Line(self.__center, to_cell.__center)
            self.__win.draw_line(red_line, "red")
        if undo:
            grey_line = Line(self.__center, to_cell.__center)
            self.__win.draw_line(grey_line, "grey")
