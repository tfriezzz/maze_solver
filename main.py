from window import *


def main():
    win = Window(800, 600)
    # my_point_1 = Point(30, 400)
    # my_point_2 = Point(55, 255)
    # my_line_1 = Line(my_point_1, my_point_2)
    # my_point_3 = Point(10, 500)
    # my_point_4 = Point(500, 600)
    # my_line_2 = Line(my_point_3, my_point_4)
    # win.draw_line(my_line_1, "red")
    # win.draw_line(my_line_2, "blue")
    test_cell = Cell(win)
    test_cell.draw(10, 50, 400, 600, "red")
    test_cell.draw(20, 70, 300, 500, "blue")
    test_cell.draw(200, 90, 500, 400, "green")
    win.wait_for_close()


if __name__ == "__main__":
    main()
