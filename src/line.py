class Line:
    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point


    def draw(self, canvas_widget, fill_color):
        canvas_widget.create_line(
            self.first_point.x_coordinate,
            self.first_point.y_coordinate,
            self.second_point.x_coordinate,
            self.second_point.y_coordinate,
            fill=fill_color,
            width=2
        )
