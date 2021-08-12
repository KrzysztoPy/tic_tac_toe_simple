from static_text_to_game.static_text import menu_option_txt, exception_value_error_txt


def view_main_menu():
    print(*menu_option_txt(), sep='\n')


def selecting_available_option():
    pass


def input_data_from_user():
    while True:
        input_data = input()
        input_data = checking_the_correctness_of_the_selection(input_data)
        if input_data:
            return input_data
            # go_to_the_selected_option(input_data)


def checking_the_correctness_of_the_selection(user_selection):
    user_selection = user_selection

    try:
        user_selection = int(user_selection)
        return user_selection
    except ValueError:
        print(exception_value_error_txt())
        return False


def go_to_the_selected_option():
    pass
