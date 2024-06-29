from window import Window
from maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(win, 40, 40, 13, 18, 40, 40)
    maze.break_entrance_and_exit()
    maze.break_walls_r()
    maze.reset_cells_visited()
    maze.solve()
    win.wait_for_close()

main()