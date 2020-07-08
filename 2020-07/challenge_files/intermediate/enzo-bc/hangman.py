# Hangman Game by Bad McProgammer!
import sys
import random
from typing import Tuple, List


def read_file(name: str) -> str:
    with open(name) as ws:
        lines = ws.read().splitlines()
        return lines[random.randint(0, len(lines) - 1)]


def print_summary(success: bool) -> str:
    if success:
        return 'you solved the hangman game \nrun again to play again'
    else:
        return 'you died, sorry!'


def prepare_variables(word: str) -> Tuple[List, int, bool, str]:
    return [], 9, True, "?" * len(word)


def check_guess(guess: str, guessed: List, lives: int, solve: str, word: str):
    if guess in guessed:
        print('you guessed that already')
    elif (guess in word) is False:
        print("that's not in the word")
        lives -= 1
    else:
        print('you got a letter')
        for index in range(len(word)):
            if word[index] == guess:
                solve = f'{solve[0:index]}{guess}{solve[index + 1:]}'
    return lives, solve


def main():
    word = read_file('../word-list.txt')
    guessed, lives, success, solve = prepare_variables(word)
    while solve != word and lives > 0:
        for index in range(len(word)):
            print(f'{solve[index]} ', end="")
        print(f'\n\nlives = {lives}\nplease guess')
        guess = input()
        lives, solve = check_guess(guess, guessed, lives, solve, word)
        guessed.append(guess)
        if lives <= 0:
            success = False
    print(print_summary(success))


if __name__ == '__main__':
    main()
