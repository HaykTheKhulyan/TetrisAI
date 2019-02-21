import screen_grab 
import input
import logic
import time
import numpy as np 


# 116, 102, 0 = yellow O
# 0, 51, 116 = blue J
# 0, 116, 25 = green S
# 116, 0, 0 = red Z
# 0, 98, 116 = blue I
# 88, 0, 116 = purple T
# 116, 67, 0 = orange L


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
    logic.define_empty_top_layer(game_grid)
    print(game_grid)
