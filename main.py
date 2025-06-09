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
    test_cell_1 = Cell(win)
    test_cell_2 = Cell(win)
    test_cell_3 = Cell(win)
    test_cell_1.draw(10, 10, 60, 60, "red")
    test_cell_2.draw(60, 60, 110, 110, "blue")
    test_cell_3.draw(120, 120, 170, 170, "pink")
    # test_cell.draw(200, 90, 500, 400, "green")
    test_cell_1.draw_move(test_cell_2, True)
    test_cell_2.draw_move(test_cell_3)
    win.wait_for_close()


if __name__ == "__main__":
    main()
