from enum import Enum
from random import randint
from collections import Counter
from typing import Any, Optional, Union, List, Tuple, Dict


def valid_subset(dice, selection) -> bool:
    if selection is None:
        selection = []
    elif type(selection) == int:
        selection = [selection]
    dice = list(dice)
    for s in selection:
        if s not in dice:
            return False
        dice.remove(s)
    return True


def remove_dice(dice, selection) -> List[int]:
    if selection is None:
        selection = []
    elif type(selection) == int:
        selection = [selection]
    copy_dice = list(dice)
    for s in selection:
        if s not in copy_dice:
            raise ValueError(f'{selection} is not a subset of {dice}')
        copy_dice.remove(s)
    return copy_dice


def reroll_dice(dice, selection) -> List[int]:
    if not valid_subset(dice, selection):
        raise ValueError(f'{selection} is not a subset of {dice}')
    dice = remove_dice(dice, selection)
    while len(dice) < 5:
        dice += [randint(1, 6)]
    return sorted(dice)


def roll_dice(how_many=5) -> List[int]:
    return sorted([randint(1, 6) for _ in range(how_many)])


def all_dice():
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            for d3 in range(1, 7):
                for d4 in range(1, 7):
                    for d5 in range(1, 7):
                        yield [d1, d2, d3, d4, d5]


def all_hands_sorted():
    return sorted({Hand(d) for d in all_dice()})


def all_hands_grouped_by_ranking(repeat_by_probability=False) -> Dict['Ranking', List['Hand']]:
    rv = {}
    for r in Ranking:
        rv[r] = []
    for dice in all_dice():
        hand = Hand(dice)
        if repeat_by_probability or hand not in rv[hand.ranking]:
            rv[hand.ranking].append(hand)
    return dict(rv)


def rankings_with_probabilities():
    counter = Counter()
    total = 0
    for dice in all_dice():
        ranking = Hand(dice).ranking
        counter[ranking] += 1
        total += 1
    assert total == 7776
    rv = dict()
    for ranking in Ranking:
        rv[ranking] = counter[ranking] / total
    return rv


class Ranking(Enum):
    NOTHING = 0
    PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

    def __lt__(self, other: Any) -> bool:
        if type(other) == Hand:
            return self < other.ranking
        if type(other) != Ranking:
            raise TypeError(f'cannot compare instance of {type(self)} < instance of {type(other)}')
        return self.value < other.value

    def __le__(self, other: Any) -> bool:
        if type(other) == Hand:
            return self <= other.ranking
        if type(other) != Ranking:
            raise TypeError(f'cannot compare instance of {type(self)} <= instance of {type(other)}')
        return self.value <= other.value

    def __gt__(self, other: Any) -> bool:
        if type(other) == Hand:
            return self > other.ranking
        if type(other) != Ranking:
            raise TypeError(f'cannot compare instance of {type(self)} > instance of {type(other)}')
        return self.value > other.value

    def __ge__(self, other: Any) -> bool:
        if type(other) == Hand:
            return self >= other.ranking
        if type(other) != Ranking:
            raise TypeError(f'cannot compare instance of {type(self)} >= instance of {type(other)}')
        return self.value >= other.value

    def __eq__(self, other: Any) -> bool:
        if type(other) == Hand:
            return self == other.ranking
        return self is other

    def __ne__(self, other: Any) -> bool:
        if type(other) == Hand:
            return self != other.ranking
        return self is not other

    def __int__(self) -> int:
        return self.value

    def __bool__(self) -> bool:
        return self.value != 0

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self):
        return hash(self.value)

    @property
    def probability(self):
        return rankings_with_probabilities()[self]

    @property
    def cumulative_probability(self):
        rv = 0.0
        for k, v in rankings_with_probabilities().items():
            if k <= self:
                rv += v
        return rv


class Hand:

    DISABLE_UNICODE = False

    @staticmethod
    def __rank_dice(dice: List[int]) -> Tuple[Ranking, List[int]]:

        # five of a kind
        if len(set(dice)) == 1:
            return Ranking.FIVE_OF_A_KIND, list(set(dice))

        counts = Counter(dice)
        counts = sorted([(v, k) for k, v in counts.items()], reverse=True)

        # four of a kind
        if len(counts) == 2 and counts[0][0] == 4 and counts[1][0] == 1:
            value = counts[0][1]
            other = counts[1][1]
            return Ranking.FOUR_OF_A_KIND, [value, other]

        # full house
        if len(counts) == 2 and counts[0][0] == 3 and counts[1][0] == 2:
            value = counts[0][1]
            other = counts[1][1]
            return Ranking.FULL_HOUSE, [value, other]

        # straight
        if set(dice) == {2, 3, 4, 5, 6}:
            return Ranking.STRAIGHT, [6]
        if set(dice) == {1, 2, 3, 4, 5}:
            return Ranking.STRAIGHT, [5]

        # three of a kind
        if len(counts) == 3 and counts[0][0] == 3 and counts[1][0] == 1 and counts[2][0] == 1:
            value = counts[0][1]
            other = counts[1][1]
            third = counts[2][1]
            return Ranking.THREE_OF_A_KIND, [value, other, third]

        # two pairs
        if len(counts) == 3 and counts[0][0] == 2 and counts[1][0] == 2 and counts[2][0] == 1:
            value = counts[0][1]
            other = counts[1][1]
            third = counts[2][1]
            return Ranking.TWO_PAIRS, [value, other, third]

        # pair
        if len(counts) == 4 and counts[0][0] == 2 and counts[1][0] == 1 and counts[2][0] == 1 and counts[3][0] == 1:
            value = counts[0][1]
            other1 = counts[1][1]
            other2 = counts[2][1]
            other3 = counts[3][1]
            return Ranking.PAIR, [value, other1, other2, other3]

        # nothing
        return Ranking.NOTHING, sorted(dice, reverse=True)

    @staticmethod
    def __validate_and_copy_dice(dice: Any,
                                 length: Optional[int] = None) -> List[int]:

        # accept none as zero dice
        if dice is None:
            if length is not None and 0 != length:
                raise ValueError(f'invalid dice: {dice}')
            return []

        # accept int as one die
        if type(dice) is int:
            if not (1 <= dice <= 6):
                raise ValueError(f'invalid dice: {dice}')
            if length is not None and 1 != length:
                raise ValueError(f'invalid dice: {dice}')
            return [dice]

        # recursive on a length 1 sequence
        if (type(dice) is tuple or type(dice) is list) and len(dice) == 1:
            return Hand.__validate_and_copy_dice(dice[0], length)

        # recursive on a hand
        if type(dice) is Hand:
            return Hand.__validate_and_copy_dice(dice.dice, length)

        # accept sequence as multiple dice
        if type(dice) is tuple or type(dice) is list:
            rv = list(dice)
            if length is not None and len(rv) != length:
                raise ValueError(f'invalid dice: {dice}')
            for die in rv:
                if type(die) is not int or not (1 <= die <= 6):
                    raise ValueError(f'invalid dice: {dice}')
            return sorted(rv)

        # reject any other type
        raise ValueError(f'invalid dice: {dice}')

    __slots__ = ['__dice', '__ranking', '__detail']
    __UNICODE_DICE = ' ' + '⚀⚁⚂⚃⚄⚅'

    def __init__(self, *dice: Union[int, List[int], 'Hand', None]):
        self.__dice = Hand.__validate_and_copy_dice(dice, 5) if dice else roll_dice(5)
        self.__ranking, self.__detail = Hand.__rank_dice(self.__dice)

    def __len__(self) -> int:
        return 5

    def __getitem__(self, item: int) -> int:
        if isinstance(item, int):
            if 0 <= item < 5:
                return self.__dice[item]
            else:
                raise IndexError(f'Hand index {item} out of bounds')
        else:
            raise TypeError('Hand index must be int')

    @property
    def dice(self):
        return list(self.__dice)

    @property
    def ranking(self):
        return self.__ranking

    @property
    def detail(self):
        return list(self.__detail)

    def re_roll(self, selection: List[int]):
        new_dice = list(self.dice)
        how_many = len(selection)
        if how_many == 0:
            return Hand(self)
        for die in selection:
            if type(die) is not int or not (1 <= die <= 6):
                raise ValueError(f'{type(die)} {die} is not a valid die')
            if die not in new_dice:
                raise ValueError(f'{self.dice} does not contain {list(selection)}')
            new_dice.remove(die)
        new_dice.extend(roll_dice(how_many))
        return Hand(*new_dice)

    def __str__(self):
        conversion = str
        if not Hand.DISABLE_UNICODE:
            conversion = lambda i: Hand.__UNICODE_DICE[i]
        if self.__ranking == Ranking.FIVE_OF_A_KIND:
            return conversion(self.__detail[0]) * 5 \
                   + '      Five of a Kind'
        if self.__ranking == Ranking.FOUR_OF_A_KIND:
            return conversion(self.__detail[0]) * 4 \
                   + ' ' + conversion(self.__detail[1]) \
                   + '     Four of a Kind'
        if self.__ranking == Ranking.FULL_HOUSE:
            return conversion(self.__detail[0]) * 3 \
                   + ' ' + conversion(self.__detail[1]) * 2 \
                   + '     Full House'
        if self.__ranking == Ranking.STRAIGHT:
            if self.__detail == [6]:
                return ''.join([conversion(i) for i in range(2, 6+1)]) + '      Straight'
            else:
                assert self.__detail == [5]
                return ''.join([conversion(i) for i in range(1, 5+1)]) + '      Straight'
        if self.__ranking == Ranking.THREE_OF_A_KIND:
            return conversion(self.__detail[0]) * 3 \
                   + ' ' + conversion(self.__detail[1]) \
                   + ' ' + conversion(self.__detail[2]) \
                   + '    Three of a Kind'
        if self.__ranking == Ranking.TWO_PAIRS:
            return conversion(self.__detail[0]) * 2 \
                   + ' ' + conversion(self.__detail[1]) * 2 \
                   + ' ' + conversion(self.__detail[2]) \
                   + '    Two Pair'
        if self.__ranking == Ranking.PAIR:
            return conversion(self.__detail[0]) * 2 \
                   + ' ' + conversion(self.__detail[1]) \
                   + ' ' + conversion(self.__detail[2]) \
                   + ' ' + conversion(self.__detail[3]) \
                   + '   Pair'
        assert self.__ranking == Ranking.NOTHING
        return conversion(self.__detail[0]) \
            + ' ' + conversion(self.__detail[1]) \
            + ' ' + conversion(self.__detail[2]) \
            + ' ' + conversion(self.__detail[3]) \
            + ' ' + conversion(self.__detail[4]) \
            + '  Nothing'

    def __repr__(self):
        return 'Hand(' + (', '.join([str(d) for d in self.__dice])) + ')'

    def __eq__(self, other: Union['Hand', Ranking]):
        if type(other) == Ranking:
            return self.__ranking == other
        if type(other) != Hand:
            return False
        return self.__dice == other.__dice

    def __ne__(self, other: Union['Hand', Ranking]):
        if type(other) == Ranking:
            return self.__ranking != other
        if type(other) != Hand:
            return False
        return self.__dice != other.__dice

    def __lt__(self, other: Union['Hand', Ranking]):
        if type(other) == Ranking:
            return self.__ranking < other
        if type(other) != Hand:
            raise TypeError(f'cannot compare instance of {type(self)} < instance of {type(other)}')
        if self.__ranking == other.__ranking:
            return self.__detail < other.__detail
        return self.__ranking < other.ranking

    def __le__(self, other: Union['Hand', Ranking]):
        if type(other) == Ranking:
            return self.__ranking <= other
        if type(other) != Hand:
            raise TypeError(f'cannot compare instance of {type(self)} <= instance of {type(other)}')
        if self.__ranking == other.__ranking:
            return self.__detail <= other.__detail
        return self.__ranking <= other.ranking

    def __ge__(self, other: Union['Hand', Ranking]):
        if type(other) == Ranking:
            return self.__ranking >= other
        if type(other) != Hand:
            raise TypeError(f'cannot compare instance of {type(self)} >= instance of {type(other)}')
        if self.__ranking == other.__ranking:
            return self.__detail >= other.__detail
        return self.__ranking >= other.ranking

    def __gt__(self, other: Union['Hand', Ranking]):
        if type(other) == Ranking:
            return self.__ranking > other
        if type(other) != Hand:
            raise TypeError(f'cannot compare instance of {type(self)} > instance of {type(other)}')
        if self.__ranking == other.__ranking:
            return self.__detail > other.__detail
        return self.__ranking > other.ranking

    def __hash__(self):
        return hash(tuple(self.__dice))
