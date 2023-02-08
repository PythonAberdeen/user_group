# Dice Poker

Dice Poker API for [Aberdeen Python User Group - Feb 2023](https://github.com/PythonAberdeen/user_group/tree/master/2023/2023-02)

## 0. Install Python and an IDE

Install Python and an IDE of your choice, or Jupyter! Any recent version: Python, 3.7, 3.8, 3.9, 3.10, or 3.11.

Ask in the group for help getting set up!

## 1. Getting Started

Download as a ZIP file [here](https://github.com/leechristie/dice-poker/releases/download/v20230207/dice-poker.zip).

Open `hello.py` or `hello.ipynb` in your IDE (or Jupyter) and run it to test if the library is working.

You should see output similar to this:

    Dice Poker package is working!
    Rolling some dice...
    ⚂⚂ ⚄ ⚁ ⚀   Pair
    ⚅⚅ ⚂⚂ ⚃    Two Pair
    second roll wins

In case the unicode dice are not very clear on your display, or don't show up properly, uncomment this line:

```python
Hand.DISABLE_UNICODE = True
```

You should see output similar to this:
    
    Dice Poker package is working!
    Rolling some dice...
    333 6 2    Three of a Kind
    22 6 5 1   Pair
    first roll wins
    
## 2. Naming Your Bot

Open `template.py` or `template.ipynb`. You should see

```python
class UntitledBot(Player):

    def name(self) -> str:
    
        # replace with a custom AI bot name
        return 'Untitled Bot'
```

Choose a unique name for your Dice Poker playing bot, e.g. *'Mr Clank'*. The class name needs to be all one word but the value returned by `name` can be any string.

```python
class MrClank(Player):

    def name(self) -> str:
    
        # replace with a custom AI bot name
        return 'Mr Clank'
```

At the bottom of the template, you'll see:

```python
# create instance of bot
our_bot = UntitledBot()
```

Change the call to your chosen bot's name.

```python
# create instance of bot
our_bot = MrClank()
```

## 3. Testing Your Bot

The template has some default behaviour coded already, so let's test it.

At the bottom of the template you will see this code:

```python
# generates a report to test the bot
result = profile_player(our_bot,
                        verbose=True,
                        roll_samples=100,
                        reroll_samples=100)
```

If you run it, you should see some output like this:

```
This code runs test on the bot to make sure it's working, and prints a table of its performance.

Running profile on player Untitled Bot . . .

Hand Delt                 <<          <          .          >         >>
----------------- ---------- ---------- ---------- ---------- ----------
NOTHING                 0.0%       2.2%       1.5%       2.2%      94.1%
PAIR                    0.0%       0.0%     100.0%       0.0%       0.0%
TWO_PAIRS               0.0%       0.0%     100.0%       0.0%       0.0%
THREE_OF_A_KIND         0.0%       0.0%     100.0%       0.0%       0.0%
STRAIGHT                0.0%       0.0%     100.0%       0.0%       0.0%
FULL_HOUSE              0.0%       0.0%     100.0%       0.0%       0.0%
FOUR_OF_A_KIND          0.0%      33.4%      16.7%      33.2%      16.7%
FIVE_OF_A_KIND          0.0%       0.0%     100.0%       0.0%       0.0%



DONE
```

What does this mean?

The bot is tested against all the posssible types of hand many times.

The first column shows what hand the bot was delt. For example, `FOUR_OF_A_KIND` means this row corresponds to when the bot was tested against a hand such as 3, 3, 3, 3, 5.

The value under `<<` is what percentage of the time the bot's choice ended up in a worse hand than 4-of-a-kind.

The value under `<` is what percentage of the time the bot's choice ended up staying 4-of-a-kind, but worse, such as 3, 3, 3, 3, 5 turning into 2, 2, 2, 2, 5 or 3, 3, 3, 3, 4.

The value under `.` is what percentage of the time the bot's choice ended up not changing the hand at all.

The value under `>` is what percentage of the time the bot's choice ended up staying 4-of-a-kind, but better, such as 3, 3, 3, 3, 5, turning into 4, 4, 4, 4, 5, or 3, 3, 3, 3, 6.

The value under `>>` is what percentage of the time the bot's choice ended up in a better hand than 4-of-a-kind (i.e. 5-of-a-kind).

## 4. Checking the Code

The function `choose_dice_to_reroll` is what controls the bot's decision on what to reroll.

```python
def choose_dice_to_reroll(self,
                          current_stakes: int,
                          available_money: int,
                          my_hand: Hand,
                          opponent_hand: Hand) -> List[int]:

    if my_hand == Ranking.NOTHING:

        # we have a bad hand, so just reroll everything
        return list(my_hand)

    if my_hand == Ranking.FOUR_OF_A_KIND:

        # when the ranking is 4-of-a-kind, e.g. 2, 2, 3, 2, 2, the detail will give 2, 3 that is the
        # number which is a set of four followed by the unmatched die (3)
        matched_four, the_other_die = my_hand.detail

        # we will reroll the other die
        return [the_other_die]

    # default case, we don't reroll anything
    return []
```

Checking the template logic, it looks like the bot takes a decision to reroll everything if the hand is raked `Ranking.NOTHING`.

It does this by converting the hand to a list using `list(my_hand)` and returning it. This tells the Dice Poker game the bot wants to reroll everything.

```python
if my_hand == Ranking.NOTHING:

    # we have a bad hand, so just reroll everything
    return list(my_hand)
```

We can see from the test this works well, 96.3% of the time (2.2% + 94.1%), the bot ends up with a better hand.

```
Hand Delt                 <<          <          .          >         >>
----------------- ---------- ---------- ---------- ---------- ----------
NOTHING                 0.0%       2.2%       1.5%       2.2%      94.1%
...
```

How can it end up with a worse hand 2.2% of the time? If the hand were:

1 2 4 5 6

And they rerolled into:
 
1 2 3 5 6

That would technically be a worse hand though both are ranked as 'Nothing'. Don't worry too much able to details of different hands of the sam type for now.

The bot also has a case for 4-of-a-kind.

We need to understand what `.detail` does.

`.detail` gives the details of the particular hand. In the case of 4-of-a-kind, the first value is the number which appears four times, and the second value is the number which appears once.

For example, is the hand is 3, 3, 3, 3, 5 then my_hand.detail gives us `3, 5`

The bot returns a list containing only the other die, e.g. in the example above [3], indicating that is should only reroll that die.

```python
if my_hand == Ranking.FOUR_OF_A_KIND:

    # when the ranking is 4-of-a-kind, e.g. 2, 2, 3, 2, 2, the detail will give 2, 3 that is the
    # number which is a set of four followed by the unmatched die (3)
    matched_four, the_other_die = my_hand.detail

    # we will reroll the other die
    return [the_other_die]
```

This seems to do quite well too. Only a third of the time, the hand is worse (though is doesn't drop below 4-of-a-kind).

```
Hand Delt                 <<          <          .          >         >>
----------------- ---------- ---------- ---------- ---------- ----------
...
FOUR_OF_A_KIND          0.0%      33.4%      16.7%      33.2%      16.7%
...
```

## 5. Playing Against the Bot

Add this code to challenge your bot to a game!

```python
challenge(our_bot,
          initial_coin=100,
          initial_stake=10,
          raise_amount=10,
          num_rounds=3)
```

You will be prompted for your name, then at each round you will be prompted to say `yes` or `no` to accept raising stakes, then input the dice you want to reroll, e.g. if your dice are 1 2 3 3 3 and you choose to reroll the 1 and the 2, you can type `1 2`.

## 6. Tips for Writing a Bot

You probably want to add cases for each ranking. The rankings are:

```python
Ranking.NOTHING
Ranking.PAIR
Ranking.TWO_PAIRS
Ranking.THREE_OF_A_KIND
Ranking.STRAIGHT
Ranking.FULL_HOUSE
Ranking.FOUR_OF_A_KIND
Ranking.FIVE_OF_A_KIND
```

To understand what `.detail` does for a given rank try creating an example in your main method in Python:

```python
example = Hand(1, 1, 2, 2, 3)
print(example.detail)
```

This prints:

```
[2, 1, 3]
```

What's happening is, it gives the larger pair `2`, then the smaller pair `1`, then the spare unpaired die `3`.

Which means for a two of a kind you could write:

```python
larger_pair, smaller_pair, other_die = example.detail
```

then if you want to reroll only the other die: you could write:

```python
return [other_die]
```

Alternatively if you wanted to reroll the smaller pair and the other die:

```python
return [smaller_pair, smaller_pair, other_die]
```

Note: if you only include `smaller_pair` once you would only reroll one of them!

Question: Which works better? Try both versions and test your bot.

## 7. Playing Two Bots Against One Another

If you have two bots `first_bot` and `second_bot`, you can have them play togethor.

For this to make sense, you might want to have two bots which run using different logic.

```python
result = play(first_bot,
              second_bot,
              initial_coin=100,
              initial_stake=10,
              raise_amount=10,
              num_rounds=3,
              verbose=True)
```

If you want to play many round, try setting `verbose=False` and `num_rounds=100`, then call `print_rounds`.

```python
result = play(first_bot,
              second_bot,
              initial_coin=100,
              initial_stake=10,
              raise_amount=10,
              num_rounds=100,
              verbose=False)
print_rounds(result, first_bot, second_bot)
```

You will get a table showing the coin held by each bot at each round until the end. e.g.

```
            Round             Bot 1             Bot 2
----------------- ----------------- -----------------
                0               100               100
                1               110                90
                2               120                80
                3               110                90
                4               120                80
                5               130                70
                6               140                60
                7               130                70
                8               140                60
                9               150                50
               10               160                40
               11               150                50
               12               170                30
               13               190                10
               14               180                20
               15               190                10
               16               180                20
               17               190                10
               18               200                 0
```

Both bots start with 100 coin, and in this example, Bot 1 easily beat Bot 2 is almost every round.

## 8. Expert Tips for Advanced Coders Only!

<details>
<summary>Click Me For Advanced Secrets</summary>

To write the best bot you might want to have your bot consider the oponent's hand.

For example:

```python
if my_hand >= opponent_hand:
```

will compare if your hand is better.

And,

```python
if my_hand.ranking >= opponent_hand.ranking:
```

will compare if the ranking is higher.

You can also take into acount `current_stakes` and `available_money` to see how in dange you are of losing.

Rankings also have `.ranking.probability` and `.ranking.cumulative_probability` which you could use to compare how good both players' rankings are.

You might notice `profile_player` returns something. We can also stop it printing with `verbose=False`.

```python
result = profile_player(our_bot,
                        verbose=False,
                        roll_samples=100,
                        reroll_samples=100)
```

We can then retrive the profile as a Python dict:

```python
{
    Ranking.NOTHING: OutcomeCount(worse_rank=0.0, worse=0.0234, same=0.0163, better=0.022175, better_rank=0.938125),
    Ranking.PAIR: OutcomeCount(worse_rank=0.0, worse=0.0, same=1.0, better=0.0, better_rank=0.0),
    Ranking.TWO_PAIRS: OutcomeCount(worse_rank=0.0, worse=0.0, same=1.0, better=0.0, better_rank=0.0),
    Ranking.THREE_OF_A_KIND: OutcomeCount(worse_rank=0.0, worse=0.0, same=1.0, better=0.0, better_rank=0.0),
    Ranking.STRAIGHT: OutcomeCount(worse_rank=0.0, worse=0.0, same=1.0, better=0.0, better_rank=0.0),
    Ranking.FULL_HOUSE: OutcomeCount(worse_rank=0.0, worse=0.0, same=1.0, better=0.0, better_rank=0.0),
    Ranking.FOUR_OF_A_KIND: OutcomeCount(worse_rank=0.0, worse=0.33111, same=0.16782, better=0.3344, better_rank=0.16667),
    Ranking.FIVE_OF_A_KIND: OutcomeCount(worse_rank=0.0, worse=0.0, same=1.0, better=0.0, better_rank=0.0)
}
```

This could be used to programatically make incrmental improvements to a bot.

Similarly, `play` also has a result object, set to `verbose=False` and access the coin per round.
  
</details>
