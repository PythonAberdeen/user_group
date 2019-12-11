# This Month's Challenge Projects

<details open>
  <summary>December 2019</summary>

## Level 1 - Fibonacci Sequence

### Problem

The [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) is defined by the following rule:

    F(1) = 1
    F(2) = 1
    F(n) = F(n-1) + F(n-2)

or, the next term is the sum of the previous two,

    1, 2, 3, 5, 8, 13, ...

Write a function which takes an integer "n" and outputs the n'th number in the Fibonacci sequence

For example:

    >>> F(6)
    13
    
    >>> F(1000)
    43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875

### Ideas for Enhancment

There are multiple different ways to implement this, have you tried at least two different ways?

Try printing out the sequence, and see how long it takes to print 1000 terms

    1
    2
    3
    5
    8
    13
    ...

Try modifying your Fibonacci function to produce the [bi-directional sequence](https://en.wikipedia.org/wiki/Fibonacci_number#Sequence_properties) meaning the function is defined for negative numbers and zero too. 

Can you modify the program to print the Tribonaci sequence (first 3 terms are `1` and the next term is the sum of the previous 3 terms) or n-bonaci sequence (first n terms are `1` and the next term is the sum of the previous n terms).

## Level 2 - Search Engine Index

### Problem

This problem is based on a previous exercise by [Python Morsels](https://www.pythonmorsels.com/).

Write a function `count_words` that accepts a string and returns a `dict` or `Counter` that has the count of each word. e.g.

    >>> count_words("fun fun what fun is python")
    {'fun': 3, 'what': 1, 'is': 1, 'python': 1}

    >>> count_words("Don't stop coding in Python")
    {"Don't": 1, 'stop': 1, 'coding': 1, 'in': 1, 'Python': 1}

### Ideas for Enhancment

Have your function ignore case, and ignore punctuation outside of words:

    >>> count_words("Don't stop coding in Python!")
    {"don't": 1, 'stop': 1, 'coding': 1, 'in': 1, 'python': 1}

Try loading text from a file and counting it's works. Have your function accept either a string, or a file.

Try scraping text from a web page (Try `requests` and `beautifulsoup` libraries), and counting the words there. But don't count the tags, only the text

    <h>Hello World</h>
    <p>"HELLO WORLD" is a fun program which makes coding fun!<p>

    {"hello": 2, 'world': 2, 'is': 1, 'a': 1, 'fun': 2, 'program': 1, 'which': 1, 'makes': 1, 'coding': 1}

Consider having your function remove [stop words](https://en.wikipedia.org/wiki/Stop_words)

    <h>Hello World</h>
    <p>"HELLO WORLD" is a fun program which makes coding fun!<p>

    {"hello": 2, 'world': 2, 'fun': 2, 'coding': 1}
    
Given a list of website URLs, and a word (say `coding`) can you find which website is mentions the work the most?

What about a list of multiple words to search for?

## Level 3 - Pascalian Puzzle

### Problem

This problem was inspired by a [Mathologer](https://www.youtube.com/watch?v=9JN5f7_3YmQ) video.

Write a program which takes a list of integers 0, 1, and 2, and displays a triangle using the following rule: If two adjacent numbers are the same (e.g. 0 and 0), the number below will be the same (0), if two adjacent numbers are different (e.g. 2 and 0), the number below will be the other number (1), i.e.:

    0 + 0 = 0
    0 + 1 = 2
    1 + 1 = 1
    1 + 2 = 0
    2 + 2 = 2
    0 + 2 = 1

Example, given the input:

    >>> print_triangle([2, 2, 0, 1, 1, 0, 0, 1, 0, 1])

Print the triangle:

    2 2 0 1 1 0 0 1 0 1
     2 1 2 1 2 0 2 2 2
      0 0 0 0 1 1 2 2
       0 0 0 2 1 0 2
        0 0 1 0 2 1
         0 2 2 1 0
          1 2 0 2
           0 1 1
            2 1
             0

Write a function which finds the final number (the bottom corner) given an input list. e.g.

    >>> get_last_number([2, 2, 0, 1, 1, 0, 0, 1, 0, 1])
    0

The input example is length `n = 10` but can be any size.

The length of the input here is `n = 10`. Did you notice that with this size of input, the final number at the bottom of the tirangle (`0`) is always the result of combining the top two corners? This is true for a size 10 triangle, but not true for all sizes of triangle.

What other sizes of triangle does this rule work for?

### Ideas for Enhancment

How efficient can you make this? You have a short-cut for some sizes of triangle, can you use this to speed up computation of other sizes?

How efficient can you make this computation in terms of CPU time, memory? How large of a triangle can you compute the last row of in a reasonable amount of time?

</details>

# Previous Months' Challenge Problems

<details>
  <summary>November 2019</summary>

## Level 1
Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

## Level 2
Have the user enter a 3-letter IATA code for an Airport (e.g LHR) and output the full name of the airport. You can get a list of the top 30  [here](https://www.world-airport-codes.com/world-top-30-airports.html). Wikipedia has a longer list [here](https://en.wikipedia.org/wiki/List_of_airports_by_IATA_and_ICAO_code).

Check that the input is three letters long - if not handle the error. 
_Hint_ - think about how you validate input (length and case), and what data structure you would use to store the code / name. 

## Level 3
Take as input opening hours as a string e.g. "Mo-Fr 08:00-12:00,13:00-17:30; Sa 08:00-12:00" and a specific DateTime and have the program tell you whether the business is open at that time or not. 

See this ([specification](https://wiki.openstreetmap.org/wiki/Key:opening_hours) ) for opening hours. 

It doesn't sound super advanced but it's kinda tricky when you get into handling errors an corner-cases and optimizing.

</details>

<details>
  <summary>October 2019</summary>

Build a functioning game of Hangman

</details>
