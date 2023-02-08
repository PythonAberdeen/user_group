#
# Random Player
#
# Example bot which randomly chooses which dice to reroll
# 50:50 per die
#

import random
from dicepoker import *


class RandomPlayer(Player):

    def name(self) -> str:

        return 'RandomPlayer'

    def accept_raise_stakes(self,
                            current_stakes: int,
                            available_money: int,
                            my_hand: Hand,
                            opponent_hand: Hand,
                            raise_amount: int) -> bool:

        return bool(random.randint(0, 1))

    def choose_dice_to_reroll(self,
                              current_stakes: int,
                              available_money: int,
                              my_hand: Hand,
                              opponent_hand: Hand) -> List[int]:

        rv = []
        for die in my_hand:
            if random.randint(0, 1):
                rv.append(die)
        return rv
