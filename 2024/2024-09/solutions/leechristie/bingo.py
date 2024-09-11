import random
from enum import Enum
from typing import Iterator


RANGES = [(1, 15), (16, 30), (31, 45), (46, 60), (61, 75)]


def balls() -> Iterator[int]:
    all_balls = list(range(1, 75 + 1))
    random.shuffle(all_balls)
    for ball in all_balls:
        yield ball


class WinType(Enum):

    NO_WIN = 0
    FULL_ROW = 1
    FULL_COL = 2
    FULL_BOTH = 3

    def __bool__(self) -> bool:
        return self.value != 0


class BingoCard:

    __slots__ = ['values']

    def __init__(self):
        values: list[tuple[int | None, bool]] = [(None, False)] * 5 * 5
        self.values = values
        for col in range(5):
            numbers = list(range(RANGES[col][0], RANGES[col][1] + 1))
            random.shuffle(numbers)
            for row, number in enumerate(numbers[:5]):
                self[row, col] = number, False
        self[2, 2] = None, True

    def __getitem__(self, key: tuple[int, int]) -> tuple[int | None, bool]:
        if type(key) != tuple or len(key) != 2:
            raise IndexError('invalid key')
        row, column = key
        if type(row) != int or not 0 <= row < 5:
            raise IndexError('invalid row')
        if type(row) != int or not 0 <= column < 5:
            raise IndexError('invalid column')
        return self.values[row * 5 + column]

    def __setitem__(self, key: tuple[int, int], value: tuple[int | None, bool]) -> None:
        if type(key) != tuple or len(key) != 2:
            raise IndexError('invalid key')
        row, column = key
        if type(row) != int or not 0 <= row < 5:
            raise IndexError('invalid row')
        if type(row) != int or not 0 <= column < 5:
            raise IndexError('invalid column')
        self.values[row * 5 + column] = value

    def __str__(self) -> str:
        rv: str = ''
        for row in range(5):
            for col in range(5):
                if col != 0:
                    rv += ' '
                value, checked = self[row, col]
                if value is None:
                    value = '  '
                else:
                    value = str(value)
                    if len(value) < 2:
                        value = ' ' + value
                if checked:
                    value = '[' + value + ']'
                else:
                    value = ' ' + value + ' '
                rv += value
            rv += '\n'
        return rv

    def check_cell(self, key: tuple[int, int]) -> None:
        if type(key) != tuple or len(key) != 2:
            raise IndexError('invalid key')
        row, column = key
        if type(row) != int or not 0 <= row < 5:
            raise IndexError('invalid row')
        if type(row) != int or not 0 <= column < 5:
            raise IndexError('invalid column')
        value, _ = self[key]
        self[key] = value, True

    def check(self, number: int) -> None:
        for row in range(5):
            for col in range(5):
                value, _ = self[row, col]
                if value == number:
                    self.check_cell((row, col))

    def __repr__(self) -> str:
        return str(self)

    def __specific_row_win(self, row) -> bool:
        for col in range(5):
            _, checked = self[row, col]
            if not checked:
                return False
        return True

    def __specific_col_win(self, col) -> bool:
        for row in range(5):
            _, checked = self[row, col]
            if not checked:
                return False
        return True

    def __row_win(self) -> bool:
        for row in range(5):
            if self.__specific_row_win(row):
                return True
        return False

    def __col_win(self) -> bool:
        for row in range(5):
            if self.__specific_col_win(row):
                return True
        return False

    def win(self) -> WinType:
        row_win = self.__row_win()
        col_win = self.__col_win()
        if row_win and col_win:
            return WinType.FULL_BOTH
        if row_win:
            return WinType.FULL_ROW
        if col_win:
            return WinType.FULL_COL
        return WinType.NO_WIN

    def clear(self) -> None:
        for row in range(5):
            for col in range(5):
                value, _ = self[row, col]
                checked = value is None
                self[row, col] = value, checked
