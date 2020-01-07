Click the arrows below to view this month's challenge problems. You can also view [previous months](/previous).

# January 2020

<details>
  <summary>Level 1 - Pig Latin Translation</summary>

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
  <summary>Level 2 - Bisection Method</summary>

### Problem

Write a function:

    def bisection(f, left, right, dp):
        ...

which returns the value of `x` (correct to `dp` decimal places) in the range `[left, right]` such that `f(x) = 0`.

You may assume that one of `f(left)` and `f(right)` is positive and the other is negative, and that `f` is a smooth continuous function (meaning the function crosses the x-axis at some point in the range `[left, right]`)

### Example usage

We want to find a value `x` (to `6` d.p.) in the range `[2.1, 2.3]` such that `x * e^(-x) - 0.25 = 0`.

    >>> import math
    >>> bisection(lambda x: x * math.exp(-x) - 0.25, 2.1, 2.3, 6)
    2.153292

The solution is 2.153292 (to 6 d.p.)

The same function has a solution in between 0 and 1; find this other solution to 8 decimal places.

### Hints

We start by considering values of `x` in the range `[left, right]`

In the example: `[left, right]` = `[2.1, 2.3]`

Now find the midpoint `mid`

In the example: `mid = 2.2`

If `f(mid) < 0 < f(right)` or `f(mid) > 0 > f(right)`, then the solution is in `[mid, right]`, we continue using the `[mid, right]`, splitting this range in half again.

If `f(left) < 0 < f(mid)` or `f(left) > 0 > f(mid)`, then the solution is in `[left, mid]`, we continue using the `[mid, right]`, splitting this range in half again.

We stop once the two end points of the range agree to dp decimal places, and return the value rounded to dp decimal places.

</details>

<details>
  <summary>Level 3 - ROT Cypher</summary>

### Problem

Write a program to encode plaintext using a rotation cypher. i.e. if the key is `5` then each character moves forward `5` places in the alphabet. (`A` -> `F`, and `Y` -> `D`) Drop all non-alphabetic characters.

Input example:

    >>> encrypt('Python Aberdeen!', 5)
    UDYMTSFGJWIJJS

Have your program split the output into chunks of a size you can choose (in the example below chunk size 4) to disguise the input further. If the length of the input is not a multiple of the chunk size, just pad out the end with randomly-chosen junk letter (here `XI` is just padding and has no meaning).

    >>> encrypt('Python Aberdeen!', 5, 4)
    UDYM TSFG JWIJ JSXI

Write a decrypt function which takes an encpyted string and key. Note that you will have lost formatting and the string will end with some junk characters, but this is okay.

    >>> encrypt('UDYM TSFG JWIJ JSXI', 5)
    PYTH ONAB ERDE ENSD

Test your decrpyption: [`CYPHER1.txt`](/2020-01/level3/CYPHER1.txt) was encoded with the key `4`, check that is decodes.

Try encrypting a large block or text, several paragraphs and saving it [in the GitHub](/2020-01/level3/).

### Ideas for Enhancment

[`CYPHER2.txt`](/2020-01/level3/CYPHER2.txt) was encoded with an unknown key.

Write a program to automatically detect and decrpty the key by explointing thayt fact that `E` is the most common letter in the English language. Have your program automatically crack the above file without a human having to guess and check keys.

</details>
