import pyscreenshot as ImageGrab
import time

# not sure why I do this but it fixes something about the DPI which led to a black screen
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

# these are the coordinates to grab from the screen
# calibrated at 67% zoom and scrolled all the way up
play_area_coords = (818, 380, 1080, 902)
next_box_coords = (1145, 440, 1265, 653)

def grab_play_area(show = False):
    """
    returns an image of the play area
        """
    img = ImageGrab.grab(bbox=play_area_coords)
    if show:
        img.show()
    return img
        
def grab_next_box(show = False):
    """
    returns an image of the box holding the next tetrominoes
    """
    
    img = ImageGrab.grab(bbox=next_box_coords)
    if show:
        img.show()
    return img