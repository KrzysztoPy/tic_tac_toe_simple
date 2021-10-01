def game_name_txt():
    return '\n Simple Tic Tac Toe \n'


def menu_option_txt():
    menu_list = ['1. Stat menu', '2. Statistic', '3. Exit']
    return menu_list


def question_about_selected_option_txt():
    return '\n Select option: '


def error_wrong_data_type_txt():
    return ' Incorrect data type. You can select only digt. Please try again.'


def error_wrong_range_of_selected_data():
    return ' Incorrect data range. You can selected option from range {} to {}. Please try again.'.format(1,
                                                                                                          menu_option_txt().__len__())


def exit_txt():
    return '\nGood bye!\n'


def starting_x_o_txt(x_or_y):
    return 'The user who selected {} starts the game.'.format(x_or_y)


def board_txt():
    return ''' _|_|_	1 2 3
 _|_|_	4 5 6
  | |	7 8 9'''


print(error_wrong_range_of_selected_data())
