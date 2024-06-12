from typing import Optional

import numpy as np


NUMBERS = ['🟩', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '▪️']


class SudokuGrid:

    WIDTH = 9
    HEIGHT = 9

    def __init__(self, data: list[list[int]]) -> None:
        self.grid = np.array(data)
        if self.grid.shape != (SudokuGrid.HEIGHT, SudokuGrid.WIDTH):
            raise ValueError(f'SudokuGrid must be {SudokuGrid.HEIGHT} by {SudokuGrid.WIDTH}')
        for row in range(SudokuGrid.HEIGHT):
            for col in range(SudokuGrid.WIDTH):
                value = data[row][col]
                if value not in range(10):
                    raise ValueError(f'SudokuGrid values must be 0 to 9')

    def __getitem__(self, item: tuple[int, int]) -> Optional[int]:
        y, x = item
        if x not in range(SudokuGrid.WIDTH) or y not in range(SudokuGrid.HEIGHT):
            raise ValueError('item index out of range')
        rv = int(self.grid[y][x])
        return rv if rv != 0 else None

    def __setitem__(self, item: tuple[int, int], value: int) -> None:
        y, x = item
        if x not in range(SudokuGrid.WIDTH) or y not in range(SudokuGrid.HEIGHT):
            raise ValueError('item index out of range')
        if value not in range(1, 10):
            raise ValueError(f'SudokuGrid values must be 1 to 9 in setting an item')
        self.grid[y][x] = value

    def __delitem__(self, item: tuple[int, int]) -> None:
        y, x = item
        if x not in range(SudokuGrid.WIDTH) or y not in range(SudokuGrid.HEIGHT):
            raise ValueError('item index out of range')
        self.grid[y][x] = 0

    def __str__(self) -> str:
        rv = ''
        for row in range(SudokuGrid.HEIGHT):
            if row in (3, 6):
                rv += NUMBERS[-1] * (9 + 2) + '\n'
            for col in range(SudokuGrid.WIDTH):
                if col in (3, 6):
                    rv += NUMBERS[-1]
                value = self[(row, col)]
                rv += NUMBERS[value] if value is not None else NUMBERS[0]
            rv += '\n'
        return rv

    def first_empty(self) -> Optional[tuple[int, int]]:
        for row in range(SudokuGrid.HEIGHT):
            for col in range(SudokuGrid.WIDTH):
                value = self[(row, col)]
                if value is None:
                    return row, col
        return None

    def __is_invalid_row(self, row: int) -> bool:
        seen = set()
        for col in range(SudokuGrid.WIDTH):
            value: Optional[int] = self[row, col]
            if value is not None:
                if value in seen:
                    return True
                seen.add(value)
        return False

    def __is_invalid_col(self, col: int) -> bool:
        seen = set()
        for row in range(SudokuGrid.HEIGHT):
            value: Optional[int] = self[row, col]
            if value is not None:
                if value in seen:
                    return True
                seen.add(value)
        return False

    def __is_invalid_block(self, first_row: int, first_col: int) -> bool:
        seen = set()
        for col in range(first_col, first_col + 3):
            for row in range(first_row, first_row + 3):
                value: Optional[int] = self[row, col]
                if value is not None:
                    if value in seen:
                        return True
                    seen.add(value)
        return False

    def is_invalid(self) -> bool:
        for row in range(self.HEIGHT):
            if self.__is_invalid_row(row):
                return True
        for col in range(self.HEIGHT):
            if self.__is_invalid_col(col):
                return True
        for row in 0, 3, 6:
            for col in 0, 3, 6:
                if self.__is_invalid_block(row, col):
                    return True
        return False

    def is_full(self):
        return self.first_empty() is None

    def is_solved(self):
        return self.is_full() and not self.is_invalid()

    def solve(self) -> bool:

        first_empty = self.first_empty()

        if first_empty is None:
            return self.is_solved()

        assert self[first_empty] is None
        for candidate in range(1, 10):
            self[first_empty] = candidate
            solved = self.solve()
            if solved:
                return True
        del self[first_empty]
        return False


EXAMPLE = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 0, 9, 5, 3, 0, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 0, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 0, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 0],
    [3, 0, 5, 2, 8, 6, 1, 7, 9]
]


def main() -> None:

    import time

    grid = SudokuGrid(EXAMPLE)
    print('Unsolved Grid:')
    print(grid)

    start = time.perf_counter()
    solved = grid.solve()
    end = time.perf_counter()
    if solved:
        assert grid.is_solved()
        print('Solved Grid:')
        print(grid)
    else:
        print('Unable to solved grid!')

    print(f'Time Taken : {end - start:.3f} sec')


if __name__ == '__main__':
    main()
