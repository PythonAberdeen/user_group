# APUG May 2022

## Code Kata

In this month's session, we will practice a "code kata".

*"Code Kata is an attempt to bring this element of practice to software development. A kata is an exercise in karate where you repeat a form many, many times, making little improvements in each. The intent behind code kata is similar. Each is a short exercise (perhaps 30 minutes to an hour long)."* - [CodeKata.com](codekata.com)

## Tips

✅ Think of difficult corner-cases for your tests

✅ Consider taking turns pair programming

✅ TDD (test-driven development) is really useful tool

✅ Write the program, start over, what different approch could you take?

## Task - WordWarp

This task is inspired by a blog post by [Robert Martin](http://thecleancoder.blogspot.com/2010/10/craftsman-62-dark-path.html).

Write a function `wordwrap` which, given an input string and line length, outputs the text in the form of a list of strings that length, for example:

```python
>>> wordwrap('The quick brown fox jumps over the lazy dog', 15)
['The quick brown',
 'fox jumps over ',
 'the lazy dog   ']
```

If there is a word which won't fit on a line at all, break it with a hyphen. Remember to count the hyphen towards the line length!

```python
>>> wordwrap('Harry cast Expelliarmus to disarm Voldemort', 10)
['Harry cast',
 'Expelliar-',
 'mus to    ',
 'disarm    ',
 'Voldemort ']
```
