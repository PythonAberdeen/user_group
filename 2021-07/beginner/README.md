# July 2021

## Beginner Challenge

### 1. Download Starter Code

This challenge will build upon existing code we have written for this exercise.

There are two version of the file (standard Python, and Jupyter), download the version you prefer to work on:

- [Standard Python Version](bank_program.py)
- [Jupyter Notebook Version](bank_program.ipynb)

### 2. Understanding the Code

The first task will be to examine the code and try to understand what it's doing.

This doesn't really mean reading it line by line. What are the methods that are defined? The global variables?

The main method (`main()` in the standard Python version, or the final cell in the Jupyter version) is the top level of the program. It will loop around until the variable `exit` is set. What does it do in this loop?

Try running the program to test it out.

### 3. Adding a New Option

You should see by now that the program presents the user will two options that can select.

The first option is to display bank balance, and the second exits.

Change option `2` (exit) to option `3` and add a new option `2`. This new option should be selectable by choosing `2` from the menu, and will call a function called `withdraw` (which you will need to create). To start with, just have this function print a message such as `Hello`, and check that its all working.

### 4. Implementing the New Option

Our withdraw method should prompt the user for a name (Hint: this is done in option `1` already, check that code), and then amount to withdraw (Hint: use our `read_integer()` function), then deduct the amount from the balance. Don't worry about going into negative balance just yet. Test that your new option works.

Then update your code so that we do check for overdraft. Don't let the balance go below zero.

### 5. More Options

What other options make sense for our bank app?

Perhaps transfers? Adding customers? Come up with your own idea and add a new option to the system!
