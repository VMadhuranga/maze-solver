import time
import random
from cell import Cell


class Maze:
    def __init__(
            self,
            window,
            x1_coordinate,
            y1_coordinate,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
        ):
        self.win = window
        self.x1_coordinate = x1_coordinate
        self.y1_coordinate = y1_coordinate
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.cells = []
        self.create_cells()


    def create_cells(self):
        for y in range(self.num_rows):
            self.cells.append([])
            for x in range(self.num_cols):
                top_left_xy_coordinates = (
                    self.x1_coordinate + self.cell_size_x * x,
                    self.y1_coordinate + self.cell_size_y * y
                )
                bottom_right_xy_coordinates = (
                    self.x1_coordinate + self.cell_size_x * (x + 1),
                    self.y1_coordinate + self.cell_size_y * (y + 1)
                )
                self.cells[y].append(Cell(self.win, top_left_xy_coordinates, bottom_right_xy_coordinates))
                self.cells[y][x].draw()
                self.animate()


    def animate(self):
        if not self.win:
            return
        
        self.win.redraw()
        time.sleep(0.05)


    def break_entrance_and_exit(self):
        entrance_cell = self.cells[0][0]
        exit_cell = self.cells[-1][-1]

        entrance_cell.has_top_wall = False
        exit_cell.has_bottom_wall = False

        entrance_cell.draw()
        exit_cell.draw()


    def break_walls_r(self, i = 0, j = 0):
        current_cell = self.cells[i][j]
        current_cell.visited = True

        while True:
            possible_directions = []
            if i - 1 >= 0:
                adjacent_top_cell = self.cells[i - 1][j]
                if not adjacent_top_cell.visited:
                    possible_directions.append(
                        {
                            "cell": adjacent_top_cell,
                            "i": i - 1,
                            "j": j,
                            "direction": "top"
                        }
                    )
            if i + 1 < len(self.cells):
                adjacent_bottom_cell = self.cells[i + 1][j]
                if not adjacent_bottom_cell.visited:
                    possible_directions.append(
                        {
                            "cell": adjacent_bottom_cell,
                            "i": i + 1,
                            "j": j,
                            "direction": "bottom"
                        }
                    )
            if j - 1 >= 0:
                adjacent_left_cell = self.cells[i][j - 1]
                if not adjacent_left_cell.visited:
                    possible_directions.append(
                        {
                            "cell": adjacent_left_cell,
                            "i": i,
                            "j": j - 1,
                            "direction": "left"
                        }
                    )
            if j + 1 < len(self.cells[i]):
                adjacent_right_cell = self.cells[i][j + 1]
                if not adjacent_right_cell.visited:
                    possible_directions.append(
                        {
                            "cell": adjacent_right_cell,
                            "i": i,
                            "j": j + 1,
                            "direction": "right"
                        }
                    )
            
            if len(possible_directions) <= 0:
                return
            
            rand_direction = possible_directions[random.randint(0, len(possible_directions) - 1)]
            possible_directions.clear()

            if rand_direction["direction"] == "top":
                current_cell.has_top_wall = False
                rand_direction["cell"].has_bottom_wall = False

            if rand_direction["direction"] == "bottom":
                current_cell.has_bottom_wall = False
                rand_direction["cell"].has_top_wall = False

            if rand_direction["direction"] == "left":
                current_cell.has_left_wall = False        
                rand_direction["cell"].has_right_wall = False

            if rand_direction["direction"] == "right":
                current_cell.has_right_wall = False
                rand_direction["cell"].has_left_wall = False

            rand_direction["cell"].draw()
            self.animate()
            self.break_walls_r(rand_direction["i"], rand_direction["j"])


    def reset_cells_visited(self):
        for y in range(len(self.cells)):
            for x in range(len(self.cells[y])):
                self.cells[y][x].visited = False


    def solve(self):
        return self.solve_r()


    def solve_r(self, i = 0, j = 0):
        self.animate()
        current_cell = self.cells[i][j]
        current_cell.visited = True
        end_cell = self.cells[-1][-1]

        if current_cell == end_cell:
            return True
        
        possible_directions = []
        if i - 1 >= 0:
            adjacent_top_cell = self.cells[i - 1][j]
            if (
                not adjacent_top_cell.visited and 
                not adjacent_top_cell.has_bottom_wall and 
                not current_cell.has_top_wall
            ):
                possible_directions.append(
                    {
                        "cell": adjacent_top_cell,
                        "i": i - 1,
                        "j": j,
                    }
                )
        if i + 1 < len(self.cells):
            adjacent_bottom_cell = self.cells[i + 1][j]
            if (
                not adjacent_bottom_cell.visited and 
                not adjacent_bottom_cell.has_top_wall and 
                not current_cell.has_bottom_wall
            ):
                possible_directions.append(
                    {
                        "cell": adjacent_bottom_cell,
                        "i": i + 1,
                        "j": j,
                    }
                )
        if j - 1 >= 0:
            adjacent_left_cell = self.cells[i][j - 1]
            if (
                not adjacent_left_cell.visited and 
                not adjacent_left_cell.has_right_wall and 
                not current_cell.has_left_wall
            ):
                possible_directions.append(
                    {
                        "cell": adjacent_left_cell,
                        "i": i,
                        "j": j - 1,
                    }
                )
        if j + 1 < len(self.cells[i]):
            adjacent_right_cell = self.cells[i][j + 1]
            if (
                not adjacent_right_cell.visited and 
                not adjacent_right_cell.has_left_wall and 
                not current_cell.has_right_wall
            ):
                possible_directions.append(
                    {
                        "cell": adjacent_right_cell,
                        "i": i,
                        "j": j + 1,
                    }
                )

        for possible_direction in possible_directions:
            current_cell.draw_move(possible_direction["cell"])
            res = self.solve_r(possible_direction["i"], possible_direction["j"])
            if res:
                return res
            current_cell.draw_move(possible_direction["cell"], True)
        return False
