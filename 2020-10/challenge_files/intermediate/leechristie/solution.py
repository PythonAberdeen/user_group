import random

class DiceSet():
    
    slots = ['dice']
    
    def __init__(self, *args):
        for die in args:
            if type(die) is not int or die < 1:
                raise ValueError(f'{die} is not a postive int')
        self.dice = list(args)
    
    def __str__(self):
        return 'DiceSet()'
    
    def __repr__(self):
        contents = str(list(sorted(self.dice))).replace('[', '').replace(']', '')
        return f'DiceSet({contents})'
    
    def __add__(self, other):
        return DiceSet(*(self.dice + other.dice))
    
    def __mul__(self, other):
        if type(other) is not int:
            raise NotImplementedError
        if other < 0:
            raise ValueError('multiplier must be postive')
        return DiceSet(*(self.dice * other))
    
    def __rmul__(self, other):
        return self * other
    
    def __sub__(self, other):
        dice = list(self.dice)
        for die in other.dice:
            if die in dice:
                dice.remove(die)
            else:
                raise ValueError(f'not enough {die}-sided dice to subtract')
        return DiceSet(*dice)
    
    def roll(self):
        rv = 0
        for die in self.dice:
            rv += random.randint(1, die)
        return rv
