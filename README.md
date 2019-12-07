# Challenge Projects
Here are a list of challenge projects by month in reverse order. Click month to show projects.

<details>
  <summary>December 2019</summary>

## Level 1

### Problem

Write a program which takes a list of integers 0, 1, and 2, and displays a triangle using the following rule: If two adjacent numbers are the same (e.g. 0 and 0), the number below will be the same (0), if two adjacent numbers are different (e.g. 2 and 0), the number below will be the other number (1), i.e.:

    0 + 0 = 0
    0 + 1 = 2
    1 + 1 = 1
    1 + 2 = 0
    2 + 2 = 2
    0 + 2 = 1

Example, given the input:

    [2, 2, 0, 1, 1, 0, 0, 1, 0, 1]

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

The input example is length `n = 10` but can be any size.

### Ideas for Enhancment

The length of the input here is `n = 10`. Did you notice that with this size of input, the final number at the bottom of the tirangle (`0`) is always the result of combining the top two corners? This is true for a size 10 triangle, but not true for all sizes of triangle. What other sizes can you find that it works for?

Write a function which finds the final number (the bottom corner) given an input list. e.g.

    f([2, 2, 0, 1, 1, 0, 0, 1, 0, 1]) = 0

How efficient can you make this? You have a short-cut for some sizes of triangle, can you use this to speed up computation of other sizes?

## Level 2
tbc


## Level 3
tbc

</details>

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
