<details>
  <summary>Pig Latin Translation</summary>

### Problem

Write a function which translates a sentence from English to Pig Latin.

A word beginning with a vowel e.g. 'apple' has '-way' appended, i.e. 'apple-way'.

A word beginning with a consonant e.g. 'banana' has the consonant moved to the end to form the suffix, i.e. 'anana-bay'

    >>> to_pig_latin('aberdeen python')
    'aberdeen-way ython-pay'

### Ideas for Enhancment

Ensure your function can handle capitalisation and punctuation.

    >>> to_pig_latin('Aberdeen Python is a fun event. We all love coding Python!')
    'Aberdeen-way ython-Pay is-way a-way un-fay event-way. e-Way all-way ove-lay oding-cay ython-Pay!'

Implement a translation from Pig Latin back to English.

    >>> from_pig_latin('Aberdeen-way ython-Pay is-way a-way un-fay event-way. e-Way all-way ove-lay oding-cay ython-Pay!')
    'Aberdeen Python is a fun event. We all love coding Python!'

Think about how to deal with ambiguity with the suffix 'way'. Should 'event-way' become 'event' or 'wevent'? Perhaps we need a dictionary?

</details>

<details>
  <summary>Level 1 - Password Strength Rater</summary>
  
  ## Password Strength Rater
  
  In this puzzle we will build a password strength rater. The exercise is split into steps, with some links to tips which will be useful if you are just getting started!
  
  ### Writing a Python Function

Write a function which takes as arguments, the user's `username` and `password` and gives a score to their password.

To start with we can just return a score of `0`.

    def rate_password(username, password):
        score = 0
        return score

Now check to see if your function works, at the moment it should always return `0`. Below, the part next to the `>>>` indicated the function call to make, and the line below indicates the expected output.

    >>> rate_password('bob', 'python')
    0
  
  Tips: [Python Functions](https://www.w3schools.com/python/python_functions.asp)
  
  ### Rating Password Length

To start with, give the user 1 point for each character in the length of the password.

|  Criteria                                                   | Score                     |
| :---------------------------------------------------------- | ------------------------: |
| Score given for length                                      |  + 1 point per character  |

Example usage:

    >>> rate_password('bob', '')
    0

    >>> rate_password('bob', 'a')
    1

    >>> rate_password('bob', 'python')
    6

Tips: [Python string length](https://www.geeksforgeeks.org/python-string-length-len/)

### Rating Character Types

Now we want to give extra points if the password contains certain types of characters. 3 points is it contains a-z, 3 points for A-Z, and 5 points for 0-9.

Remember to add all of these togethor with the length score!

For example, `Pass42word` contains 10 characters (a score of 10), plus 2 (for a-z), plus 3 (for A-Z), plus 5 (for 0-9), giving 20 points.

A password will be graded using the following criteria:

|  Criteria                                                   | Score                     |
| :---------------------------------------------------------- | ------------------------: |
| Score given for length                                      |  + 1 point per character  |
| Contains at least 1 lower-case letter (a-z)                 |  + 2 points               |
| Contains at least 1 upper-case letter (A-Z)                 |  + 3 points               |
| Contains at least 1 digit (0-9)                             |  + 5 points               |

    >>> rate_password('bob', 'Pass42word')
    20
    
    >>> rate_password('bob', 'pass42word')
    17
    
    >>> rate_password('bob', '12345')
    5

Try writing some other test cases to check your function works.

Tips: [How to check if character in string is a letter? Python](https://stackoverflow.com/questions/15558392/how-to-check-if-character-in-string-is-a-letter-python)

### More Characters

Next, lets add for more character checks.

If the password contains any spaces, give 5 extra points, and any characters **not** in a-z, A-Z, or 0-9, or spaced, give an extra 10 points.

|  Criteria                                                   | Score                     |
| :---------------------------------------------------------- | ------------------------: |
| Score given for length                                      |  + 1 point per character  |
| Contains at least 1 lower-case letter (a-z)                 |  + 2 points               |
| Contains at least 1 upper-case letter (A-Z)                 |  + 3 points               |
| Contains at least 1 digit (0-9)                             |  + 5 points               |
| Contains a space                                            |  + 5 points               |
| Contains any other character                                |  + 10 points              |

This password gets 10 points for containing a character not listed above (plus 9 for length)

    >>> rate_password('bob', 'おはようございます')
    19

This one get's 5 points for having at least one space (plus remember the other critera)

    >>> rate_password('bob', 'Bob cat 猫')
    29
    
### Penalty

Finally, let's add a penalty for including the username in the password. If the pasword contians the username (even in a different casing) the score loses 15 points!

|  Criteria                                                   | Score                     |
| :---------------------------------------------------------- | ------------------------: |
| Score given for length                                      |  + 1 point per character  |
| Contains at least 1 lower-case letter (a-z)                 |  + 2 points               |
| Contains at least 1 upper-case letter (A-Z)                 |  + 3 points               |
| Contains at least 1 digit (0-9)                             |  + 5 points               |
| Contains a space                                            |  + 5 points               |
| Contains any other character                                |  + 10 points              |
| Contains username (case-insensitive)                        |  - 15 points              |
| Minimum score                                               |     0 points              |

    >>> rate_password('bob', 'BoX cat 猫')
    29
    
    >>> rate_password('bob', 'BoB cat 猫')
    14

Limit the minimum score to 0, so under the other rules, this would get a score of 3+2-15 = -10, but we want to scores to start at 0. So any negative score turns into 0.

    >>> rate_password('bob', 'bob')
    0

    >>> rate_password('bob', 'bobbobbobbob')
    0

    >>> rate_password('bob', 'bobbobbobbobbob')
    2

Tips: [How to Check if a Python String Contains Another String?](https://www.afternerd.com/blog/python-string-contains/)

Tips: [Python String Methods: str(), upper(), lower(), count(), find(), replace() & len()](https://thehelloworldprogram.com/python/python-string-methods/)

</details>
