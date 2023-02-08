#
# Burrito
#
# AI started at the APUG meetup
#

from dicepoker import *


class Burrito(Player):

    def name(self) -> str:

        return 'Burrito'

    def accept_raise_stakes(self,
                            current_stakes: int,
                            available_money: int,
                            my_hand: Hand,
                            opponent_hand: Hand,
                            raise_amount: int) -> bool:

        # we can compare our current hand to the opponent
        if my_hand >= opponent_hand:

            # accept the raise - we're winning so far
            return True

        else:

            # don't accept the raise - we're probably losing this round
            return False

    def choose_dice_to_reroll(self,
                              current_stakes: int,
                              available_money: int,
                              my_hand: Hand,
                              opponent_hand: Hand) -> List[int]:

        if my_hand == Ranking.NOTHING:

            # we have a bad hand, so just reroll everything
            return list(my_hand)

        if my_hand == Ranking.PAIR:

            pair, large, med, small = my_hand.detail

            return [large, med, small]

        if my_hand == Ranking.FOUR_OF_A_KIND:

            # when the ranking is 4-of-a-kind, e.g. 2, 2, 3, 2, 2, the detail will give 2, 3 that is the
            # number which is a set of four followed by the unmatched die (3)
            matched_four, the_other_die = my_hand.detail

            # we will reroll the other die
            return [the_other_die]

        if my_hand == Ranking.FULL_HOUSE:

            if opponent_hand == Ranking.FOUR_OF_A_KIND:
                triple, pair = my_hand.detail
                return [pair, pair]

        # default case, we don't reroll anything
        return []
