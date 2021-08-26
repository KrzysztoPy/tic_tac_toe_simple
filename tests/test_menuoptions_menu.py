from main_menu.menu import *


# from unittest.mock import patch
# @patch('main_menu.menu.get_input_data', return_value='z')


def test_checking_the_correctness_of_the_selection_wrong_input_data_0():
    result = checking_the_correctness_of_the_selection('z')
    assert result == None


def test_checking_the_correctness_of_the_selection_correct_input_data_0():
    result = checking_the_correctness_of_the_selection('0')
    assert result != None


def test_checking_the_correctness_of_the_selection_correct_input_data_1():
    result = checking_the_correctness_of_the_selection('-10')
    assert result != None


def test_checking_the_correctness_of_the_selection_correct_input_data_2():
    result = checking_the_correctness_of_the_selection('5')
    assert result != None


def test_checking_the_correctness_of_the_range_wrong_range_0():
    result = checking_the_correctness_of_the_range(-1)
    assert result == None


def test_checking_the_correctness_of_the_range_wrong_range_1():
    result = checking_the_correctness_of_the_range(0)
    assert result == None


def test_checking_the_correctness_of_the_range_wrong_range_3():
    result = checking_the_correctness_of_the_range(4)
    assert result == None


def test_checking_the_correctness_of_the_range_wrong_range_4():
    result = checking_the_correctness_of_the_range(7)
    assert result == None


def test_checking_the_correctness_of_the_range_correct_range_0():
    result = checking_the_correctness_of_the_range(1)
    assert result != None


def test_checking_the_correctness_of_the_range_correct_range_1():
    result = checking_the_correctness_of_the_range(3)
    assert result != None
