import pyautogui
import random

def random_drop():
    my_str_list = []
    
    if random.random() > 0.5:
        for _ in range(0, random.randint(0, 5)):
                my_str_list.append("left")
    else:
        for _ in range(0, random.randint(0, 5)):
            my_str_list.append("right")
    my_str_list.append("space")
    pyautogui.typewrite(my_str_list, interval=0.05)
