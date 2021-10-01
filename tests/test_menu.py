from main_menu.main_menu.menu_options import *
from unittest.mock import patch


@patch('xyz.xyz.checking_the_correctness_of_the_selection')
def test_processing_of_external_data_first_is_false(mock_checking_the_correctness_of_the_selection):
    mock_checking_the_correctness_of_the_selection.return_value = None
    result = data_analysis_for_compilance_with_the_guidelines('mock_none')
    assert result is None


# @patch('xyz.xyz.checking_the_correctness_of_the_selection') mock_checking_the_correctness_of_the_selection
def test_processing_of_external_data_first_is_true_sec_is_false():
    # mock_checking_the_correctness_of_the_selection.return_value = 4
    result = data_analysis_for_compilance_with_the_guidelines('0')
    assert result == None


def test_processing_of_external_data_first_and_sec_is_true_select_opt_1():
    result = data_analysis_for_compilance_with_the_guidelines('1')
    assert result == 1


def test_processing_of_external_data_first_and_sec_is_true_select_opt_2():
    result = data_analysis_for_compilance_with_the_guidelines('2')
    assert result == 2


def test_processing_of_external_data_first_and_sec_is_true_select_opt_3():
    result = data_analysis_for_compilance_with_the_guidelines('3')
    assert result == 3


def test_checking_the_correctness_of_the_selection_wrong_input_data_0():
    result = check_which_user_data_is_integer('z')
    assert result is None


def test_checking_the_correctness_of_the_selection_correct_input_data_0():
    result = check_which_user_data_is_integer('0')
    assert result is not None


def test_checking_the_correctness_of_the_selection_correct_input_data_1():
    result = check_which_user_data_is_integer('-10')
    assert result is not None


def test_checking_the_correctness_of_the_selection_correct_input_data_2():
    result = check_which_user_data_is_integer('5')
    assert result is not None


def test_checking_the_correctness_of_the_selection_correct_input_data_2():
    result = check_which_user_data_is_integer(None)
    assert result is None


def test_checking_the_correctness_of_the_selection_correct_input_data_2():
    result = check_which_user_data_is_integer('')
    assert result is None


def test_checking_the_correctness_of_the_range_wrong_range_0():
    result = checking_the_correctness_of_the_range(-1)
    assert result is None


def test_checking_the_correctness_of_the_range_wrong_range_1():
    result = checking_the_correctness_of_the_range(0)
    assert result is None


def test_checking_the_correctness_of_the_range_wrong_range_3():
    result = checking_the_correctness_of_the_range(4)
    assert result is None


def test_checking_the_correctness_of_the_range_wrong_range_4():
    result = checking_the_correctness_of_the_range(7)
    assert result is None


def test_checking_the_correctness_of_the_range_correct_range_0():
    result = checking_the_correctness_of_the_range(1)
    assert result is not None


def test_checking_the_correctness_of_the_range_correct_range_1():
    result = checking_the_correctness_of_the_range(3)
    assert result is not None
