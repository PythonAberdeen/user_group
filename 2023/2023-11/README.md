# Gradual Static Typing in Python

This is a placeholder page for the coding challenges for November 2023 relating to *Gradual Static Typing in Python*

## Installing mypy

For all challenges, you should first install `mypy`.

Using `pip`:
```
pip install mypy
```

If you are using `conda` instead, you may need to add `conda-forge` first:
```
conda config --add channels conda-forge
conda install mypy
```

**We strongly recommend using a recent version of Python** as the syntax for type hinting slightly changes between version. The example syntax given in the slides should work on Python 3.10, 3.11, and 3.12. If you are on an older verion of Python, the type hint cheat sheet will help you find the correct syntax for your version.

## Type Hint Cheat Sheet

Check [the official cheat sheet for mypy](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) for help!

## Aberdeen Python User Group Slack

By the way, you should join the [Slack](https://join.slack.com/t/codethecity/shared_invite/zt-ebfpmtdt-wMnHGebBCNJTCEInaYCwNw) for CodeTheCity and say hi in the `#apug` channel!

## Challenge 1 - Beginner

Download this challenge file [challenge1.py](https://raw.githubusercontent.com/PythonAberdeen/user_group/master/2023/2023-11/challenge1.py).

You are *not* intended to run the Python code.

Your task is to add type hints to each of the functions, and show that `mypy` detects all of the invalid calls.

To run `mypy` in the terminal, type:
```
mypy challenge1.py
```

Each function has correct and incorrect examples of calling it.

By default, since there are no type hints, `mypy` will not find any errors.

After you add type hints, all 4 incorrect calls should be detected as errors, and all correct calls should not.

## Challenge 2 - Intermediate

Download this challenge file [challenge2.py](https://raw.githubusercontent.com/PythonAberdeen/user_group/master/2023/2023-11/challenge2.py).

This is a small program which reads takes a string and finds the median of the number in the string.

Unfortunatly, the program is not correct and will raise an error when run!

Your job is *not* to manually find the mistakes, but rather, type hint the program so that `mypy` can find the mistake for you!

## Challenge 3 - Advanced

For this challenge, you must write a program demonstrait and test out the advanced features of type hinting in Python.

This could include:

- Classes with forward references
- Generics
- Generators
- Callables passed to higher order functions

Refer to the mypy cheat sheet, and get creative.
