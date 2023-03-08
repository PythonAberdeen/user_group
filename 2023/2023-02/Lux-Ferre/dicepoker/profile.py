import sys
from collections import namedtuple
from random import randint
from typing import Any, List

from dicepoker import Player, Hand, Ranking, all_hands_grouped_by_ranking

Outcome = namedtuple("OutcomeCount", "worse_rank worse same better better_rank")


def __sum_outcome(a: Outcome, b: Outcome) -> Outcome:
    return Outcome(worse_rank=a.worse_rank + b.worse_rank,
                   worse=a.worse + b.worse,
                   same=a.same + b.same,
                   better=a.better + b.better,
                   better_rank=a.better_rank + b.better_rank)


def __mean_outcome(outcome: Outcome) -> Outcome:
    total = sum(outcome)
    return Outcome(worse_rank=outcome.worse_rank / total,
                   worse=outcome.worse / total,
                   same=outcome.same / total,
                   better=outcome.better / total,
                   better_rank=outcome.better_rank / total)


def __sample_outcome(current_hand: Hand,
                     sample_size: int,
                     selection: List[int]) -> Outcome:
    if selection:
        worse_rank = 0
        worse = 0
        same = 0
        better = 0
        better_rank = 0
        for _ in range(sample_size):
            new_hand = current_hand.re_roll(selection)
            if new_hand.ranking > current_hand.ranking:
                better_rank += 1
            elif new_hand.ranking < current_hand.ranking:
                worse_rank += 1
            elif new_hand < current_hand:
                worse += 1
            elif new_hand > current_hand:
                better += 1
            else:
                same += 1
        return Outcome(worse_rank=worse_rank, worse=worse, same=same, better=better, better_rank=better_rank)
    else:
        return Outcome(worse_rank=0, worse=0, same=sample_size, better=0, better_rank=0)


def __print_heading() -> None:
    print("{: <17} {: >10} {: >10} {: >10} {: >10} {: >10}"
          .format('Hand Delt', '<<', '<', '.', '>', '>>'))
    print("{: <17} {: >10} {: >10} {: >10} {: >10} {: >10}"
          .format('-'*17, '-'*10, '-'*10, '-'*10, '-'*10, '-'*10))


def __print_row(ranking: Ranking, outcome: Outcome) -> None:
    rank_name = ranking.name
    wr_pc = f'{outcome.worse_rank * 100.0:>3.1f}%'
    worse_pc = f'{outcome.worse * 100.0:>3.1f}%'
    same_pc = f'{outcome.same * 100.0:>3.1f}%'
    better_pc = f'{outcome.better * 100.0:>3.1f}%'
    br_pc = f'{outcome.better_rank * 100.0:>3.1f}%'
    print("{: <17} {: >10} {: >10} {: >10} {: >10} {: >10}"
          .format(rank_name, wr_pc, worse_pc, same_pc, better_pc, br_pc))


def sanitize_selection(selection: Any) -> List[int]:
    if selection is None:
        return []
    if type(selection) == int:
        return [selection]
    if type(selection) == Hand:
        return selection.dice
    if type(selection) == tuple or type(selection) == list:
        for i in selection:
            if type(i) != int:
                raise TypeError('dice selection contained type ' + str(type(i))
                                + ', expected: None, int, list[int], tuple[int], Hand')
        return list(selection)
    raise TypeError(f'dice selection was type {type(selection)}, expected: None, int, list[int], tuple[int], Hand')


def profile_player(player: Player,
                   verbose: bool,
                   roll_samples: int,
                   reroll_samples: int) -> dict:
    last = None
    last_rv = None
    if verbose:
        print(f'\nRunning profile on player {player.name()} . . .\n')
    try:
        hands_by_ranking = all_hands_grouped_by_ranking(repeat_by_probability=False)
        rv = {r: None for r in Ranking}
        first_row = True
        for ranking, possible_hands in hands_by_ranking.items():
            outcome = Outcome(worse_rank=0, worse=0, same=0, better=0, better_rank=0)
            for my_hand in possible_hands:
                for _ in range(roll_samples):
                    last = None
                    last_rv = None
                    current_stakes = randint(1, 20) * 10
                    available_money = randint(1, 20) * 10
                    opponent_hand = Hand()
                    last = current_stakes, available_money, my_hand, opponent_hand
                    selection = player.choose_dice_to_reroll(current_stakes,
                                                             available_money,
                                                             my_hand,
                                                             opponent_hand)
                    last_rv = selection
                    selection = sanitize_selection(selection)
                    outcome = __sum_outcome(outcome, __sample_outcome(my_hand,
                                                                      reroll_samples,
                                                                      selection))
            outcome = __mean_outcome(outcome)
            if verbose:
                if first_row:
                    __print_heading()
                __print_row(ranking, outcome)
            first_row = False
            rv[ranking] = outcome
        if verbose:
            print('\n\n')
            print('DONE\n')
        return rv
    except KeyboardInterrupt:
        print('\n\n(action cancelled by user)', file=sys.stderr)
        sys.exit(0)
    except Exception as ex:
        print(f'\n\nEXCEPTION:  {ex}')
        if last is not None:
            current_stakes, available_money, my_hand, opponent_hand = last
            args = f'{current_stakes}, {available_money}, {repr(my_hand)}, {repr(opponent_hand)}'
            print(f'CALL:       choose_dice_to_reroll({args})')
        if last_rv is not None:
            print(f'RETURNED:   {last_rv}')
        sys.exit(1)
