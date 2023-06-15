from dicepoker import Hand


def hello_dice() -> None:
    """
    Test function to check that Dice Poker is working!
    """

    print('Dice Poker package is working!')
    print('Rolling some dice...')

    first = Hand()
    second = Hand()

    print(first)
    print(second)

    if first > second:
        print("first roll wins")
    elif second > first:
        print("second roll wins")
    else:
        print("it's a tie!")
