# 2021-03 Beginner Challenge

## Background

Mad Libs is a word game played as a party game, where player are prompted to come up with types of words, without knowing the context they will be used in, for example:

    verb (present tense, e.g. brush): paint
    noun: cat

Then once they have come up with words, the sentence is reveled with their chosen words in place:

    Be careful not to paint the cat when you are tidying your room!

The origonal template (not known to the players was:

    Be careful not to [verb (present tense, e.g. brush)] the [noun] when you are tidying your room!

## Task

Your task is to implement a game of Mad Libs, the game will load a template from a file (this template is hidden from the players), then prompt for each word type. The players will input their answers, and once all slots in the tmeplate have been filled, the final text will be revealed.

## Some Starter Hints

These hints may be useful to get started.

<details>
<summary>HINT: Code to read a text file to a variable!</summary>

    with open('madlib.txt', 'r') as file:
        text = file.read().replace('\n', '')

</details>

<details>
<summary>HINT: Code to prompt the user to type something!</summary>

    answer = input('Please input something here:')

</details>

<details>
<summary>HINT: Code to print a paragraph with line wrap!</summary>

    from textwrap import wrap

    for line in wrap(text, 80):
        print(line)

</details>

## Some Mad Libs Templates

- [Mad Libs 0 - Tidying (Example Above)](madlibs0.txt)
- [Mad Libs 1 - March](madlibs1.txt)
- [Mad Libs 2 - Computers](madlibs2.txt)
- [Ian's Mad Lib 0](ian0.txt)
- [Ian's Mad Lib 1](ian1.txt)
- [Ian's Mad Lib 2](ian2.txt)
- [Ian's Mad Lib 3](ian3.txt)
- [Example Used At Event - Python Aberdeen](python.txt)
