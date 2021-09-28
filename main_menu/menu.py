from main_menu.menu_options.static_text.menu_options_text import \
    game_name_txt, menu_option_txt, \
    question_about_selected_option_txt, wrong_range_txt
from main_menu.menu_options.exit_game import exit_game


def selecting_an_action_option():
    while True:
        print(game_name_txt())
        print(*menu_option_txt(), sep='\n')
        input_data = input(question_about_selected_option_txt())
        go_to_the_selected_option(processing_of_external_data(input_data))


def processing_of_external_data(input_data):
    is_integer = checking_the_correctness_of_the_selection(input_data)

    if is_integer or is_integer == 0:
        if checking_the_correctness_of_the_range(is_integer):
            return is_integer


def checking_the_correctness_of_the_selection(user_selection):
    try:
        user_selection = int(user_selection)
        return user_selection
    except (ValueError, TypeError):
        print(wrong_range_txt())
        return None


def checking_the_correctness_of_the_range(is_integer):
    if 0 < is_integer < 4:
        return is_integer
    else:
        print(wrong_range_txt())
        return None


def go_to_the_selected_option(selected_option):
    if selected_option == 1:
        # start_game()
        return 1

    elif selected_option == 2:
        # score_board()
        return 2
    elif selected_option == 3:
        exit_game()
