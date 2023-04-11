from abc import ABC, abstractmethod
from typing import List
from dicepoker import Hand


class Player(ABC):

    def __str__(self):
        return self.name()

    def __repr__(self):
        return self.name()

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def accept_raise_stakes(self,
                            current_stakes: int,
                            available_money: int,
                            my_hand: Hand,
                            opponent_hand: Hand,
                            raise_amount: int) -> bool:
        pass

    @abstractmethod
    def choose_dice_to_reroll(self,
                              current_stakes: int,
                              available_money: int,
                              my_hand: Hand,
                              opponent_hand: Hand) -> List[int]:
        pass




class Human(Player):

    @staticmethod
    def __read_non_empty_str(message: str, redo_message: str = None) -> str:
        if redo_message is None:
            redo_message = message
        rv = input(message)
        while not rv.strip():
            rv = input(redo_message)
        return rv

    @staticmethod
    def __to_bool(value: str) -> bool:
        value = value.strip().lower()
        if value in ('y', 'ye', 'yes'):
            return True
        if value in ('n', 'no'):
            return False
        raise ValueError(f'invalid bool: {value}')

    @staticmethod
    def __read_bool(message: str) -> bool:
        while True:
            try:
                rv = Human.__read_non_empty_str(message)
                rv = Human.__to_bool(rv)
                return rv
            except ValueError:
                print("Error: Required input is 'yes' or 'no'.")

    @staticmethod
    def __read_subset(message: str, hand: Hand, redo_message: str) -> List[int]:
        first = True
        while True:
            try:
                rv = Human.__read_non_empty_str(message if first else redo_message, redo_message)
                if rv == 'all':
                    return list(hand)
                if rv == 'keep':
                    return []
                rv = rv.replace(',', ' ').replace(';', ' ').replace('"', ' ').replace("'", ' ')
                while '  ' in rv:
                    rv = rv.replace('  ', ' ')
                rv = rv.strip()
                rv = [int(e) for e in rv.split(' ')]
                hand.re_roll(rv)  # invoke the validation code, raises ValueError if invalid
                return rv
            except ValueError:
                first = False
                print("Error: Required input is any valid subset of your dice, or 'all' or 'keep'")

    __slots__ = ['__name', '__first_round']

    def __init__(self):
        self.__name = Human.__read_non_empty_str('What is you name, human? ')
        self.__first_round = True

    def name(self) -> str:
        return self.__name

    def accept_raise_stakes(self,
                            current_stakes: int,
                            available_money: int,
                            my_hand: Hand,
                            opponent_hand: Hand,
                            raise_amount: int) -> bool:
        print(f'You have {available_money} coin available (excludes the current stake of {current_stakes})')
        return Human.__read_bool(f'Accept raising stakes from {current_stakes} to {current_stakes + raise_amount}? ')

    def choose_dice_to_reroll(self,
                              current_stakes: int,
                              available_money: int,
                              my_hand: Hand,
                              opponent_hand: Hand) -> List[int]:
        display_hand = ' '.join([str(e) for e in my_hand])
        short_message = f"Your hand is: {display_hand}\nWhich dice will you reroll? "
        long_message = f"Choose dice to reroll.\n" \
                       + f"Input your selection as a list of integers.\n" \
                       + f" e.g. '5' to reroll one 5.\n" \
                       + f"      '1 1 3' to reroll two 1s and one 3.\n" \
                       + f"You must choose a subset of your current hand.\n" \
                       + f"To reroll everything you can type 'all'.\n" \
                       + f"To keep your current dice you can type 'keep'.\n" \
                       + f"Your hand is: {display_hand}\n" \
                       + f"Which dice will you reroll? "
        if self.__first_round:
            rv = Human.__read_subset(long_message, my_hand, long_message)
        else:
            rv = Human.__read_subset(short_message, my_hand, long_message)
        self.__first_round = False
        return rv
