from os import system, name
from random import choice

## Expanding from KJ's solution to add lizard and verbs

def clear():
    # for windows
    if name == 'nt':
        system('cls')
    # for mac and Linux
    else:
        system('clear')

"""Using dictionary as suggested by @0x1ac"""
### Only records wins, e.g. rock wins over scissors
wins_over = {
    'paper': (['rock','spock'],
              ['covers', 'disproves']),
    'rock':(['scissors', 'lizard'],
            ['blunts', 'crushes']),
    'scissors':(['paper','lizard'],
                ['cuts', 'decapitates']),
    'spock':(['rock','scissors'],
             ['vaporizes', 'smashes']),
    'lizard':(['paper', 'spock'],
              ['eats', 'poisons'])
            }

options = list(wins_over.keys())
all_options = options + ['exit']
p1_result, p2_result = 0, 0

def how(w, l):
    return wins_over[w][1][wins_over[w][0].index(l)]


def rps(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()
    if p1==p2:
        return 'Tie', ''
    elif p2 in (wins_over[p1][0]):
        return 'Player 1', how(p1, p2)
    else: 
        return 'Player 2', how(p2, p1)


while True:
    clear()
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
    w, h = rps(p1_choice, p2_choice)
    print(w, end='')
    if w == 'Player 1':
        print(f' wins. {p1_choice.capitalize()} {h} {p2_choice}.')
        p1_result += 1
    elif w == 'Player 2':
        print(f' wins. {p2_choice.capitalize()} {h} {p1_choice}.')
        p2_result += 1

    input()

