import random


class DiceSet:

    def __init__(self, *args):
        for rg in args:
            if rg < 1 or type(rg) is not int:
                raise ValueError(f'{rg} is not a positive integer')

        self.dice = args

    def __repr__(self):
        if len(self.dice) == 1:
            return 'DiceSet(' + str(self.dice[0]) + ')'

        return 'DiceSet' + str(self.dice)

    def roll(self):
        return sum([random.randint(1, k) for k in self.dice])

    def __add__(self, other):
        return DiceSet(*(self.dice + other.dice))

    def __mul__(self, other):
        return DiceSet(*(self.dice * other))

    def __getitem__(self, item):
        return DiceSet(self.dice[item])

    def count(self, side):
        return self.dice.count(side)

def main():
    # negative_dice = DiceSet(1.1)
    one_dice = DiceSet(6, 30, 100)
    two_dice = DiceSet(5)
    # print(one_dice.roll())
    # print(one_dice + two_dice)
    # print(one_dice * 5)

    # for die in one_dice:
    #     print(die.roll())

    print(one_dice.count(100))

if __name__ == '__main__':
    main()
