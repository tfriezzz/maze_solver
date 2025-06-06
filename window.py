from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack(fill=BOTH)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line_instance, fill_color):
        line_instance.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas_instance, fill_color=""):
        self.canvas_instance = canvas_instance
        self.fill_color = fill_color
        canvas_instance.create_line(
            self.point_1.x,
            self.point_1.y,
            self.point_2.x,
            self.point_2.y,
            fill=fill_color,
            width=2,
        )


def main():
    win = Window(800, 600)
    my_point_1 = Point(30, 400)
    my_point_2 = Point(55, 255)
    my_line_1 = Line(my_point_1, my_point_2)
    my_point_3 = Point(10, 500)
    my_point_4 = Point(500, 600)
    my_line_2 = Line(my_point_3, my_point_4)
    win.draw_line(my_line_1, "red")
    win.draw_line(my_line_2, "blue")
    win.wait_for_close()


if __name__ == "__main__":
    main()
