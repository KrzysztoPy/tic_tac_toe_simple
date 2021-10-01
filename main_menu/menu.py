from main_menu.menu_options.static_text.menu_options_text import *

question_about_selected_option_txt, error_wrong_data_type_txt
from main_menu.menu_options.start_game import New_match
from main_menu.menu_options.exit_game import exit_game


def selecting_an_action_option():
    while True:
        print(game_name_txt())
        print(*menu_option_txt(), sep='\n')
        input_data = input(question_about_selected_option_txt())


def data_analysis_for_compilance_with_the_guidelines(user_data):
    user_input_data = check_which_user_data_is_integer(user_data)

    if user_input_data or user_input_data == 0:
        if checking_the_correctness_of_the_range(user_input_data):
            return user_input_data


def check_which_user_data_is_integer(user_data):
    try:
        user_data = int(user_data)
        return user_data
    except (ValueError, TypeError):
        print(error_wrong_data_type_txt())
        return None


def checking_the_correctness_of_the_range(is_integer):
    if 0 < is_integer < 4:
        return is_integer
    else:
        print(error_wrong_range_of_selected_data())
        return None


def go_to_the_selected_option(user_selection):
    if user_selection == 1:
        new_gameplay = New_match()
        # new_gameplay.

        # draw_who_play_x_and_who_o()
        return 1

    elif user_selection == 2:
        # score_board()
        return 2
    elif user_selection == 3:
        exit_game()

