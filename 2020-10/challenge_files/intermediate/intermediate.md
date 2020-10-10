# Intermediate Challenge - Oct 2020

In this challenge, we will design a class called `DiceSet` which reprsents a set of dice. There can be zero or more dice in the set. Dice can have different number of sides, and there can be more than one die of each type.

## Construction and Representation

We should be able to construct a `DiceSet` by specifying zero or more dice.

The dice are specified by giving the number of sides. For example a set with two 20-sided dice and one 6-sided die is constructed with `DiceSet(6, 20, 20)` (the order is not important, so `DiceSet(20, 6, 20)` also works).

**Hint:** Use `\*args` on the constructor to allow any number of arguments.

When we get the `repr` *(either by using the `repr()` function explictly, or just using an output cell if you're using Jupyter or interactive mode)* we get an unabiguous representation of the type as shown below.

    >>> DiceSet()
    DiceSet()

    >>> DiceSet(20)
    DiceSet(20)
    
    >>> DiceSet(6, 6, 20, 6, 100, 20)
    DiceSet(6, 6, 6, 20, 20, 100)

## Validation

Dice can only have a postive integer number of sides, otherwise, the constructor should throw a `ValueError`.

    >>> DiceSet(-1)
    ValueError: -1 is not a postive int
    
    >>> DiceSet(3.14)
    ValueError: 3.14 is not a postive int

## Rolling

You should be able to roll the dice in the dice set and return the total using the `.roll()` method.

    >>> single = DiceSet(20)
    >>> single.roll()
    4
    >>> single.roll()
    12
    >>> single.roll()
    8
    
If there is more than one die, 

    >>> set_one = DiceSet(20, 6)
    >>> set_one.roll()
    19
    >>> set_one.roll()
    5
    >>> set_one.roll()
    22

An empty dice set will always roll 0.

    >>> empty = DiceSet()
    >>> empty.roll()
    0

## Adding Dice Sets

You should be able to add two `DiceSet` objects to create a new `DiceSet` object.

    >>> DiceSet(20) + DiceSet(6, 100)
    DiceSet(6, 20, 100)

## Multiplying a Dice Set

If a `DiceSet` is multiplied by an interger we get a new DiceSet where the contents are multiplied by that integer.

If the multiplier is a negative, you should raise `ValueError`.

    >>> DiceSet(20) * 5
    DiceSet(20, 20, 20, 20, 20)

    >>> 3 * DiceSet(100)
    DiceSet(100, 100, 100)

    >>> 0 * DiceSet(100)
    DiceSet()

    >>> -1 * DiceSet(100)
    ValueError: multiplier must be postive

## Subtracting Dice Sets

If dice set `b` is a subset (or equal to) dice set `a`, we should be able to create a new `DiceSet` object from `a - b`. Otherwise a `ValueError` is thrown.

    >>> a = DiceSet(20) * 10 + DiceSet(6) * 3
    >>> b = DiceSet(20) * 8
    >>> a - b
    DiceSet(6, 6, 6, 20, 20)

    >>> b - a
    ValueError: not enough 20-sided dice to subtract
    
## String Representation

Python has `repr`, which typically gives a string which is the same the string you would use to construct the object, but also there is `str` which is usually a more friendly string.

For the empty dice set we'll keep the same representation (this is similar to the way the `str` of the empty set is `set()`), but for other sets, we'll make more friendly strings

    >>> str(DiceSet())
    'DiceSet()'

    >>> str(DiceSet(20))
    'd20'
    
    >>> str(DiceSet(6, 20))
    'd6 + d20'

    >>> str(DiceSet(20) * 2)
    '2d20'
    
    >>> str(DiceSet(20, 100, 100, 1000, 20))
    '2d20 + 3d100'

## More Ideas?

What else could we do with this project? Here are some ideas:

- Allow converting to a list or dict `list(DiceSet(6, 20))`
- Enable mutation `.add_die(6)` changes the set of dice
- `.contains_die(20)` returns `True` if there is a d20 in the set
- `.count(20)` returns the number of d20s in the set
- Add str parsing to the constructor e.g. `DiceSet('2d20 + 3d100')`
- All the set to be iterated returning a one-die set each time, so `for d in DiceSet(20, 20, 100)` works as if `for d in [DiceSet(20), DiceSet(20), DiceSet(100)]`

Are there any other ideas you can think of? Try to make whatever you do feel *Pythonic*.
