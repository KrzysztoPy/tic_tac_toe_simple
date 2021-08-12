from main_menu.menu import input_data_from_user, checking_the_correctness_of_the_selection
from static_text_to_game.static_text import exception_value_error_txt
from unittest.mock import patch


def test_input_data_from_user():
    # results = input_data_from_user()
    # assert results == True
    pass


def test_checking_the_correctness_of_the_selection():
    string_letter_sample = ('x', 'h')
    string_special_character_sample_2 = ('+', '*')
    string_integer_data = ('2', '33')
    for i in string_letter_sample:
        result = checking_the_correctness_of_the_selection(i)
        assert result == False

    for i in string_special_character_sample_2:
        result = checking_the_correctness_of_the_selection(i)
        assert result == False

    for i in string_integer_data:
        result = checking_the_correctness_of_the_selection(i)
        assert result != False
