from os import system, name
from random import choice
import pandas as pd


def clear():
    # for windows
    if name == 'nt':
        system('cls')
    # for mac and Linux
    else:
        system('clear')


options = ['paper', 'rock', 'scissors', 'spock']
all_options = options + ['exit']
p1_result, p2_result = 0, 0

"""Using dictionary as suggested by @0x1ac"""
### Only records wins, e.g. rock wins over scissors
wins_over = {
            'paper':['rock','spock'],
            'rock':['scissors'],
            'scissors':['paper','spock'],
            'spock':['rock','scissors']
            }


def rps(p1: str, p2: str) -> str:
    global p1_result, p2_result
    p1 = p1.lower()
    p2 = p2.lower()

    if p1==p2:
        return 'Tie'
    elif p2 in (wins_over[p1]):
        p1_result += 1
        return 'Player 1 won!'
    else: 
        p2_result += 1
        return 'Player 2 won!'


while True:
    p1_choice, p2_choice = '', ''
    while p1_choice.lower() not in all_options:
        p1_choice = input('Player 1 > ')
        clear()

    if 'exit' in p1_choice.lower():
        print(f'You won {p1_result} games\nPC won {p2_result} games')
        break

    # second player computer code
    p2_choice = choice(options)

    # second player human code
    # while p2_choice.lower() not in options:
    #     p2_choice = input('Player 2 > ')
    #     clear()

    print(f'> Player 1 chose {p1_choice}\n')
    print(f'> Player 2 chose {p2_choice}\n')
    print(f'{rps(p1_choice, p2_choice)}')

    input()
    clear()
