from dicepoker import *
Hand.DISABLE_UNICODE = True


# Create Your Dice Poker AI
class Moonpouncer(Player):

    def name(self) -> str:

        # replace with a custom AI bot name
        return 'Moonpouncer'

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

            return [small]

        if my_hand == Ranking.TWO_PAIRS:
            first_pair, second_pair, remaining = my_hand.detail

            return remaining

        if my_hand == Ranking.THREE_OF_A_KIND:
            triple, large, small = my_hand.detail

            return [large, small]

        if my_hand == Ranking.STRAIGHT:
            return []

        if my_hand == Ranking.FULL_HOUSE:

            triple, pair = my_hand.detail

            return []

        if my_hand == Ranking.FOUR_OF_A_KIND:

            # when the ranking is 4-of-a-kind, e.g. 2, 2, 3, 2, 2, the detail will give 2, 3 that is the
            # number which is a set of four followed by the unmatched die (3)
            matched_four, the_other_die = my_hand.detail

            # we will reroll the other die
            return [the_other_die]

        if my_hand == Ranking.FIVE_OF_A_KIND:
            return  []

        # default case, we don't reroll anything
        return []

class Thunderchild(Player):

    def name(self) -> str:

        # replace with a custom AI bot name
        return 'Thunderchild'

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

        if my_hand.ranking < opponent_hand.ranking:
            take_risks = True
        else:
            take_risks = False

        if my_hand == Ranking.NOTHING:

            # we have a bad hand, so just reroll everything
            return list(my_hand)

        if my_hand == Ranking.PAIR:
            pair, large, med, small = my_hand.detail

            if take_risks:
                return [small, med, large]
            else:
                return [small]

        if my_hand == Ranking.TWO_PAIRS:
            first_pair, second_pair, remaining_die = my_hand.detail

            return remaining_die

        if my_hand == Ranking.THREE_OF_A_KIND:
            triple, large, small = my_hand.detail

            return [large, small]

        if my_hand == Ranking.STRAIGHT:
            if take_risks:
                return list(my_hand)
            else:
                return []

        if my_hand == Ranking.FULL_HOUSE:

            triple, pair = my_hand.detail

            if take_risks:
                return [pair]
            else:
                return []

        if my_hand == Ranking.FOUR_OF_A_KIND:

            # when the ranking is 4-of-a-kind, e.g. 2, 2, 3, 2, 2, the detail will give 2, 3 that is the
            # number which is a set of four followed by the unmatched die (3)
            matched_four, the_other_die = my_hand.detail

            # we will reroll the other die
            return [the_other_die]

        if my_hand == Ranking.FIVE_OF_A_KIND:
            return  []

        # default case, we don't reroll anything
        return []

if __name__ == '__main__':

    # create instance of bot
    first_bot = Moonpouncer()
    second_bot = Thunderchild()

    # generates a report to test the bot
    # result = profile_player(our_bot,
    #                        verbose=True,
    #                        roll_samples=100,
    #                        reroll_samples=100)

    result = play(first_bot,
                  second_bot,
                  initial_coin=100,
                  initial_stake=10,
                  raise_amount=10,
                  num_rounds=100,
                  verbose=True)
    print_rounds(result, first_bot, second_bot)
