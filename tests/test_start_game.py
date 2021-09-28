from main_menu.menu_options.start_game import start_game, PLAYER_X, PLAYER_Y
from main_menu.menu_options.static_text.menu_options_text import starting_x_o_txt

from random import randint
from unittest.mock import patch


@patch('random.randint')
def test_start_game(mock_randint):
    mock_randint.return_value = 0
    result = start_game()
    # print(result)
    print(starting_x_o_txt(PLAYER_X))
    # assert result == print(starting_x_o_txt(PLAYER_X))


