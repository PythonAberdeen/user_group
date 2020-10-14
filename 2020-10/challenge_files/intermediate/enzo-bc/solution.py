#%%
import random


class DiceSet:

    def __init__(self, *args):
        self.dices = []
        for arg in args:
            if isinstance(arg, int) and arg > 1:
                self.dices.append(arg)
            else:
                raise ValueError('{} is not a positive int'.format(arg))

    def __repr__(self):
        return 'DiceSet({})'.format(', '.join([str(x) for x in self.dices]))

    def __str__(self):
        return 'DiceSet({})'.format(', '.join([str(x) for x in self.dices]))

    def __add__(self, other):
        return DiceSet(*(self.dices + other.dices))

    def __sub__(self, other):
        result = self.dices
        try:
            for item in other.dices:
                result.remove(item)
        except ValueError:
            raise ValueError('not enough {}-sided dice to subtract'.format(item))

        return DiceSet(*result)

    def __mul__(self, other):
        if isinstance(other, int) and other > 1:
            return DiceSet(*(self.dices * other))
        else:
            raise ValueError('multiplier must be postive')

    def __rmul__(self, other):
        if isinstance(other, int) and other > 1:
            return DiceSet(*(self.dices * other))
        else:
            raise ValueError('multiplier must be postive')

    def roll(self):
        total = 0
        for dice in self.dices:
            total += random.randint(1, dice)
        return total

    def count(self, number):
        return self.dices.count(number)


#%%
DiceSet()
#%%
DiceSet(-1)
#%%
DiceSet(3.14)
#%%
DiceSet(3)
#%%
DiceSet(5, 6, 7).roll()
#%%
DiceSet(2, 3, 4) + DiceSet(2, 4)
#%%
DiceSet(2) * 5
#%%
5 * DiceSet(3)
#%%
-1 * DiceSet(2)
#%%
str(DiceSet(2))
#%%
a = DiceSet(20) * 10 + DiceSet(6) * 3
b = DiceSet(20) * 8
a - b
#%%
b - a
#%%
DiceSet(20, 4, 20, 5, 20).count(20)