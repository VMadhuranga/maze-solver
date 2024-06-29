from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.root_widget = Tk()
        self.root_widget.title("Maze solver")

        self.canvas_widget = Canvas(master=self.root_widget, background="white", width=self.width, height=self.height)
        self.canvas_widget.pack(fill=BOTH)


    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()


    def draw_line(self, line, fill_color):
        line.draw(self.canvas_widget, fill_color)


    def wait_for_close(self):
        self.root_widget.mainloop()
