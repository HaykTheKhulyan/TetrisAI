import screen_grab
import numpy as np

# y = 4, add 26 each row
# x = 13, add 26 each col


# 116, 102, 0 = yellow O
# 0, 51, 116 = blue J
# 0, 116, 25 = green S
# 116, 0, 0 = red Z
# 0, 98, 116 = blue I
# 88, 0, 116 = purple T
# 116, 67, 0 = orange L


def create_grid_array():
    grid_image = screen_grab.grab_play_area()
    grid_image.show()
    grid = grid_image.load()
    game_grid = np.zeros((20, 10))

    #for col in range(0, 10):
    #    for row in range(0, 20):
    #        grid_color = grid[13 + (col * 26), 4 + (row * 26)]
    #        if grid_color == (0, 0, 0):
    #            game_grid[row][col] = 'b'
    #        elif grid_color == (116, 102, 0):
    #            game_grid[row][col] = 'O'
    #        elif grid_color == (0, 51, 116):
    #            game_grid[row][col] = 'J'
    #        elif grid_color == (0, 116, 25):
    #            game_grid[row][col] = 'S'
    #        elif grid_color == (116, 0, 0):
    #            game_grid[row][col] = 'Z'
    #        elif grid_color == (0, 98, 116):
    #            game_grid[row][col] = 'I'
    #        elif grid_color == (88, 0, 116):
    #            game_grid[row][col] = 'T'
    #        elif grid_color == (116, 67, 0):
    #            game_grid[row][col] = 'L'

    for col in range(0, 10):
        for row in range(0, 20):
            if grid[13 + (col * 26), 4 + (row * 26)] != (0, 0, 0):
                game_grid[row][col] = 1
    
    return game_grid

def define_empty_top_layer(game_grid):
    solid_found = False
    row = 1

    for col in range(0, 10):
        row = 1
        solid_found = False
        while not solid_found :
            if row == 19:
                game_grid[row][col] = 2
                solid_found = True
            if row == 19 or game_grid[row][col] == 1:
                game_grid[row - 1][col] = 2
                solid_found = True
            row += 1
