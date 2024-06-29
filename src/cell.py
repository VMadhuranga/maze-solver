from line import Line
from point import Point


class Cell:
    def __init__(
            self, 
            window,
            top_left_xy_coordinates,
            bottom_right_xy_coordinates,
            has_top_wall = True,
            has_bottom_wall = True,
            has_left_wall = True,
            has_right_wall = True,
        ):
        self.win = window
        self.top_left_xy_coordinates = top_left_xy_coordinates
        self.bottom_right_xy_coordinates = bottom_right_xy_coordinates
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.visited = False


    def draw(self, fill_color = "black"):
        top_left_x, top_left_y = self.top_left_xy_coordinates
        bottom_right_x, bottom_right_y = self.bottom_right_xy_coordinates

        top_line = Line(Point(top_left_x, top_left_y), Point(bottom_right_x ,top_left_y))
        bottom_line = Line(Point(top_left_x, bottom_right_y), Point(bottom_right_x, bottom_right_y))
        left_line = Line(Point(top_left_x, top_left_y), Point(top_left_x, bottom_right_y))
        right_line = Line(Point(bottom_right_x, top_left_y), Point(bottom_right_x, bottom_right_y))

        top_line_fill_color = fill_color
        bottom_line_fill_color = fill_color
        left_line_fill_color = fill_color
        right_line_fill_color = fill_color

        if not self.has_top_wall:
            top_line_fill_color = "white"
        if not self.has_bottom_wall:
            bottom_line_fill_color = "white"
        if not self.has_left_wall:
            left_line_fill_color = "white"
        if not self.has_right_wall:
            right_line_fill_color = "white"

        self.win.draw_line(top_line, top_line_fill_color)
        self.win.draw_line(bottom_line, bottom_line_fill_color)
        self.win.draw_line(left_line, left_line_fill_color)
        self.win.draw_line(right_line, right_line_fill_color)
        

    def draw_move(self, to_cell, undo = False):        
        self_cell_top_left_x, self_cell_top_left_y = self.top_left_xy_coordinates
        self_cell_bottom_right_x, self_cell_bottom_right_y = self.bottom_right_xy_coordinates
        to_cell_top_left_x, to_cell_top_left_y = to_cell.top_left_xy_coordinates
        to_cell_bottom_right_x, to_cell_bottom_right_y = to_cell.bottom_right_xy_coordinates

        self_cell_center_x = abs(self_cell_top_left_x + self_cell_bottom_right_x) / 2
        self_cell_center_y = abs(self_cell_top_left_y + self_cell_bottom_right_y) / 2
        to_cell_center_x = abs(to_cell_top_left_x + to_cell_bottom_right_x) / 2
        to_cell_center_y = abs(to_cell_top_left_y + to_cell_bottom_right_y) / 2

        center_line = Line(Point(self_cell_center_x, self_cell_center_y), Point(to_cell_center_x, to_cell_center_y))
        fill_color = "red"

        if undo:
            fill_color = "grey"

        self.win.draw_line(center_line, fill_color)


    def update_walls(
            self, 
            top_wall,
            bottom_wall,
            left_wall,
            right_wall
        ):
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall


    def get_walls_info(self):
        return [
            self.has_top_wall,
            self.has_bottom_wall,
            self.has_left_wall,
            self.has_right_wall
        ]
