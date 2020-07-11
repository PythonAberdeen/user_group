# Notes

## Counting occurences

The two solutions take different approaches to counting the occurences of the words in the given text. `solution.py` uses `.count()` on the full string where `group2.py` first splits the string into a list of words and then counts the occurences fo the name strings in that list of strings.

For the given text these different approaches give the same results but they could differ for different text. If the text included the word "bobbin" then this would could as an occurence of "Bob" with the `solution.py` method, but would not with the `group2.py` approach. Conversely we probably do want `Bob's` to count as an occurence of `Bob`, the `solution.py` approach will count this, but `group2.py` method won't.

This kind of thing comes up a lot in any programming. There are often a lot more edge cases than you might initially think so this is a common source of bugs somewhere down the line when we do encounter data with that edge case.

## List of Unique names

The given list of names has a couple of duplicates in it. Python includes [set](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset): a collection that enforces each element be unique, so this is an easy way to get a list of unique names by turning our list with duplicates into a set and then back into a list. Note that sets are unorderred so if we cared about preserving the order of the names from the original list we would have to use another approach here.

## Specifying data file

The `group2.py` solution can take the filename for the data file from a  command line argument. If an argument is not provided then the default `page.txt` is used. This is a very simple example of using command line arguments, if we had anything more complicated it would be better to use one of the modules for parsing command line arguments (e.g. [argparse](https://docs.python.org/3.3/library/argparse.html)) rather than directly accessing `sys.argv`. In a "real" program it would also be useful to do some error checking or exception catching in case the user had provided a filename that doesn't exist (or that the program can't access).

## List comprehension

There is a common pattern where we want to build a list of elements that are the processed version of items from another list. Python offers a method of doing this in one line with (list comprehension)[https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions].

Here we have the traditional `for` loop method of creating `clean_names` in `solution.py` and the list comprehension methos in `group2.py`

## lambda expressions

The `sorted()` function (or `.sort()` method if we were sorting in place) accepts a function that it will use to process the elements to extract the key to sort by. Both solutions here use [lambda expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions) to create anonymous functions for this purpose. This functionality could equivalently have been written using `def` to create these functions with a name. Whether a lambda expression or a `def` is the best solution is mostly a matter of preference for the people reading or writing the code (the python interpretter doesn't care). lambda expressions are useful where the defined function is only going to be used in this one place and is small enough that it can be embedded where it is used without throwing off the readability of that code.

## Nmaed tuples

`group2.py` uses [named tuples](https://pymotw.com/2/collections/namedtuple.html) to store the counts. In the first pass writing this we used normal tuples and were then accessing the name or count by index. This approach can be brittle as it relys on the programmer remember what order they picked for the name and count fields each time these are accessed. This gets worse if we have more fields in our tuple or are using them in more places, further from where they are defined (so it is harder to look back at the definition to check what index we want). Named tuples let the programmer access the fields by name and have the computer keep track of what index that name corresponds to.

## f strings

`solution2.py` uses [f strings](https://realpython.com/python-f-strings/) to construct its output.

## Unpacking

The `for` loop in `group2.py` makes use of [tuple unpacking](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences) to assign to multiple variables with one statement.