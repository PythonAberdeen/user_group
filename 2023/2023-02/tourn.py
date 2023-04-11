#
# Tournament
#
# Play one bot vs another
#

from dicepoker import *
from randomplayer import RandomPlayer
from burrito import Burrito

if __name__ == '__main__':

    bu = Burrito()
    rp = RandomPlayer()
    result = play(bu,
                  rp,
                  initial_coin=100,
                  initial_stake=10,
                  raise_amount=10,
                  num_rounds=100,
                  verbose=False)
    print_rounds(result, bu, rp, suspense=0.5)
