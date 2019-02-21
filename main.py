import screen_grab 
import input
import logic
import time
import numpy as np 

#where every tetrominoe starts when it spawns
tetrominoe_starting_block_coords = (120, 40)

if __name__ == "__main__":
    time.sleep(5)
    #while (True):
    #    time.sleep(0.05)
    #    img1 = screen_grab.grab_play_area()
    #    img2 = img1.load()
    #    print(img2[tetrominoe_starting_block_coords])
    #    input.random_drop()
    game_grid = logic.create_grid_array()
    print(game_grid)
