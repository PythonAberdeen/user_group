import pytest

from hangman import read_file, print_summary, prepare_variables, check_guess


def test_read_file():
    assert read_file('test.txt') == 'test'


def test_print_summary_success():
    assert print_summary(True) == 'you solved the hangman game \nrun again to play again'


def test_print_summary_failure():
    assert print_summary(False) == 'you died, sorry!'


def test_prepare_variables():
    assert prepare_variables('test') == ([], 9, True, '????')


def test_check_guess_guessed_already():
    assert check_guess('e', ['e'], 9, '?e??', 'test') == (9, '?e??')


def test_check_guess_not_in_word():
    assert check_guess('a', ['e'], 9, '?e??', 'test') == (8, '?e??')


def test_check_guess_good_guess():
    assert check_guess('t', ['e'], 8, '?e??', 'test') == (8, 'te?t')
