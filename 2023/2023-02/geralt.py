#
# Geralt
#
# Example bot by Dr Lee A. Christie
#

from dicepoker import *


class Geralt(Player):

    def name(self) -> str:
        return "Geralt"

    def accept_raise_stakes(self,
                            current_stakes: int,
                            available_money: int,
                            my_hand: Hand,
                            opponent_hand: Hand,
                            raise_amount: int) -> bool:

        # accept raise if my hand is better or the same rank
        if my_hand.ranking >= opponent_hand.ranking:
            return True
        else:
            return False

    def choose_dice_to_reroll(self,
                              current_stakes: int,
                              available_money: int,
                              my_hand: Hand,
                              opponent_hand: Hand) -> List[int]:

        if my_hand == Ranking.NOTHING:
            # re-roll everything
            return list(my_hand)

        if my_hand == Ranking.PAIR:
            # re-roll the three unpaired dice
            pair, l, m, s = my_hand.detail
            return [l, m, s]

        if my_hand == Ranking.TWO_PAIRS:
            # re-roll the unpaired die
            large_pair, small_pair, other = my_hand.detail
            return [other]

        if my_hand == Ranking.THREE_OF_A_KIND:
            # re-roll the two other dice
            three, l, s = my_hand.detail
            return [l, s]

        if my_hand == Ranking.FOUR_OF_A_KIND:
            # re-roll the other die
            four, other = my_hand.detail
            return [other]

        # keep everything if straight, full house, or five of a kind
        return []
