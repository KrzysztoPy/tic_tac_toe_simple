import random
from main_menu.menu_options.static_text.menu_options_text import starting_x_o_txt

PLAYER_X = 'X'
PLAYER_Y = 'Y'


# 0 = O , 1 = X
def start_game():
    if random.randint(0, 1):
        print(starting_x_o_txt(PLAYER_X))
    else:
        print(starting_x_o_txt(PLAYER_Y))


def draw_who_starts():
    pass



