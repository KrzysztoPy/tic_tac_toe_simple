from main_menu.menu import *
from unittest.mock import patch
from unittest.mock import Mock


@patch('main_menu.menu.checking_the_correctness_of_the_selection')
def test_processing_of_external_data_first_is_false(mock_checking_the_correctness_of_the_selection):
    mock_checking_the_correctness_of_the_selection.return_value = None
    result = processing_of_external_data('mock_none')
    assert result is None


# @patch('main_menu.menu.checking_the_correctness_of_the_selection') mock_checking_the_correctness_of_the_selection
def test_processing_of_external_data_first_is_true_sec_is_false():
    # mock_checking_the_correctness_of_the_selection.return_value = 4
    result = processing_of_external_data('4')
    assert result == None


def test_processing_of_external_data_first_and_sec_is_true_select_opt_1():
    result = processing_of_external_data('1')
    assert result == 1


def test_processing_of_external_data_first_and_sec_is_true_select_opt_2():
    result = processing_of_external_data('2')
    assert result == 2


def test_processing_of_external_data_first_and_sec_is_true_select_opt_3():
    result = processing_of_external_data('3')
    assert result == 3


def test_checking_the_correctness_of_the_selection_wrong_input_data_0():
    result = checking_the_correctness_of_the_selection('z')
    assert result is None


def test_checking_the_correctness_of_the_selection_correct_input_data_0():
    result = checking_the_correctness_of_the_selection('0')
    assert result is not None


def test_checking_the_correctness_of_the_selection_correct_input_data_1():
    result = checking_the_correctness_of_the_selection('-10')
    assert result is not None


def test_checking_the_correctness_of_the_selection_correct_input_data_2():
    result = checking_the_correctness_of_the_selection('5')
    assert result is not None


def test_checking_the_correctness_of_the_selection_correct_input_data_2():
    result = checking_the_correctness_of_the_selection(None)
    assert result is None


def test_checking_the_correctness_of_the_selection_correct_input_data_2():
    result = checking_the_correctness_of_the_selection('')
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
