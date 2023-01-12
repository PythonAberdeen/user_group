from os import system, name
from random import choice
from collections import OrderedDict

## Expanding from KJ's solution to add more options (extensions from umop.com/rps.htm) and verbs

def clear():
    # for windows
    if name == 'nt':
        system('cls')
    # for mac and Linux
    else:
        system('clear')

"""Using dictionary as suggested by @0x1ac"""
### Only records wins, e.g. rock wins over scissors
d = OrderedDict()
d['paper'] =  (['rock','air', 'water', 'gun',  'devil'],
               ['covers', 'fans', 'floats on', 'outlaws', 'rebukes'])
d['rock'] = (['scissors', 'fire', 'sponge', 'human', 'wolf'],
             ['blunts', 'pounds out', 'crushes', 'crushes', 'crushes'])
d['scissors'] = (['paper','sponge', 'air', 'human', 'wolf'],
                  ['cuts', 'cuts', 'swishes through', 'cuts', 'cuts'])
d['air'] = (['fire', 'rock', 'water', 'gun', 'devil'],
             ['blows out', 'erodes', 'evaporates', 'tarnishes', 'chokes'])
d['fire'] = (['scissors', 'paper', 'sponge', 'human', 'wolf'],
             ['melts', 'burns', 'burns', 'burns', 'burns'])
d['sponge'] = (['paper', 'air', 'water', 'gun', 'devil'],
             ['soaks', 'uses', 'absorbs', 'cleans', 'cleanses'])
d['water'] = (['rock', 'fire', 'scissors', 'gun', 'devil'],
               ['erodes', 'puts out', 'rusts', 'rusts', 'drowns'])
d['gun'] = (['rock', 'fire', 'scissors', 'human', 'wolf'],
            ['targets', 'fires', 'outclasses', 'shoots', 'shoots'])
d['human'] = (['sponge', 'paper', 'air', 'water', 'wolf'],
              ['cleans with', 'writes on', 'breathes', 'drinks', 'tames'])
d['wolf'] = (['sponge', 'paper', 'air', 'water', 'devil'],
             ['chews up', 'chews up', 'breathes', 'drinks', 'bites'])
d['devil'] = (['rock', 'fire', 'scissors', 'gun', 'human'],
              ['hurls', 'breathes', 'is immune to', 'is immune to', 'possesses'])
wins_over = d


options = list(wins_over.keys())[:5]
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

def rps_list(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()
    if p1==p2:
        return 'Tie'
    else:
        diff = options.index(p1) - options.index(p2)
        tot = len(options)
        if tot % 2 == 0:
            tot += 1
        if diff % tot % 2 == 0:
            return 'Player 1'
        else:
            return 'Player 2'
if True:
    for p1 in options:
        for p2 in options:
            print(f'{p1} vs {p2}')
            if not rps(p1, p2)[0] == rps_list(p1, p2):
                print(f'WRONG: {rps(p1, p2)} {rps_list(p1, p2)}')
    input()
        

while True:
    clear()
    p1_choice, p2_choice = '', ''
    while p1_choice.lower() not in all_options:
        p1_choice = input(f'{", ".join(all_options)}?\n>')
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

