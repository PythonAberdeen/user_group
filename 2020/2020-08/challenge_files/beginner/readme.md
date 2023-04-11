# Beginner challenge August 2020

Create a program which prompts the user to input player's name and score (integer between 0 and 100), then displays a sorted scoreboard in decending order.

Tip: Use `input()` to prompt the user (this will read from console or if using Jupyter, will display a text box).

Example input (the text "Name:" and "Score:" is the printed prompt not part of the user's input)

    Name: Alice
    Score: 45
    Name: Bob
    Score: 78
    Name: Carol
    Score: 82
    Name: Dan
    Score: 30
    Name: Erin
    Score: 89

Output:

    Erin     89
    Carol    82
    Bob      78
    Alice    45
    Dan      30

Think about how to terminate the loop. For example you could stop when the user enters a blank name.

You should validate the score and re-prompt the user if they input an invalid score.

    Name: Alice
    Score: 101
    Invalid input!
    Score: -1
    Invalid input!
    Score: Forty-Two
    Invalid input!
    Score: 42

You may want to enhance the scoreboard by adding numbering

    1.    Erin     89
    2.    Carol    82
    3.    Bob      78
    4.    Alice    45
    5.    Dan      30

You could also add support for ties, if there is a tie, then the number should not be printed.
For example, here Carol and Bob are both in joint second, with the next player, Alice being in 4th.

    1.    Erin     89
    2.    Carol    82
          Bob      82
    4.    Alice    45
    5.    Dan      30
