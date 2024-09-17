import numpy as np


def generate_bingo_column(
    min_val: int,
    max_val: int,
    is_middle: bool = False,
) -> np.array:
    options: np.array = np.array(range(min_val, max_val + 1))
    column: np.array

    if is_middle:
        column = np.random.choice(options, size=4, replace=False)
        column = np.insert(column, 2, 0)
    else:
        column = np.random.choice(options, size=5, replace=False)

    return column


def generate_bingo_card() -> np.array:

    bingo_card = np.empty(shape=(5, 5), dtype=int)

    bingo_card[0] = generate_bingo_column(1, 15)
    bingo_card[1] = generate_bingo_column(16, 30)
    bingo_card[2] = generate_bingo_column(31, 45, is_middle=True)
    bingo_card[3] = generate_bingo_column(46, 60)
    bingo_card[4] = generate_bingo_column(61, 75)

    return bingo_card


def print_bingo_card(card: np.array) -> None:

    print("B  I  N  G  O")
    for k in range(5):
        for i in range(5):
            print(f"{card[i][k]:2}", end=" ")
        print("")


if __name__ == "__main__":
    bingo_card = generate_bingo_card()
    print_bingo_card(bingo_card)
