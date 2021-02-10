from itertools import cycle, islice
from math import floor

options = ['paper', 'rock', 'scisors', 'spock', 'lizard']
n_option = len(options)
assert n_option % 2 == 1
n_win = floor(n_option/2)
win_to_conds = []
for x in range(n_win):
    idx_win_to = x * 2 + 1
    win_to_conds.append(islice(cycle(options),idx_win_to, idx_win_to+n_option))

p1_win_cond = {o: win_conds for o, *win_conds in zip(options, *win_to_conds)}

def RPS(p1, p2):
    if p1 == p2:
        return 'tie'
    elif p1 in p1_win_cond[p1]:
        return 'p1 win'
    else:
        return 'p2 win'

print(RPS('lizard', 'rock'))
