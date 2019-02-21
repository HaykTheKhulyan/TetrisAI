import screen_grab
import numpy as np

def create_grid_array():
    grid_image = screen_grab.grab_play_area()
    grid_image.show()
    grid = grid_image.load()
    game_grid = np.zeros((20, 10))

    for col in range(0, 10):
        for row in range(0, 20):
            if(grid[15 + (col * 25), 25 + (row * 26)] != (0, 0, 0)):
                game_grid[row][col] = 1
    
    return game_grid

    