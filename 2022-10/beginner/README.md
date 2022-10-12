# APUG October 2022 Beginner Challenge

Today we will create a fuction in Python. 

## What are Python functions?

Functions are a block of statements or tasks which, when we pass some value to them will return a result which is consistent and predictable. 

We put some commonly or repeatedly done tasks together (to make a function) so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again. 

What we pass values to the function we call those values _parameters_.

Most times the function _RETURNS_ a value when all statement in the function have been executed. 

It is good practice to include a docstring which describes what the function does

The syntax is
<pre>
def function_name (parameters):
	"""docstring""" (optional but good practice)
	#statement(s)
	RETURN expression
</pre>pre>

## Create your first function

Create a Python function that accepts a single word and returns the number of vowels in that word. Vowels are a, e, i, o, and u. 

Test the function with several words. 

Does it get it right every time? What about if the word has no vowels (eg flyby or nymphs)?

## Create a second function
Create a Python function that accepts a string which can contain any type and number of characters. 

Your function should count the number of Xs and the number of Os in the string. 

It should then return a boolean value of either True or False. See [this page](https://pythonguides.com/python-booleans/) if you haven't come across Python booleans before. 

If the count of Xs and Os are equal, then the function should return True. Ignore upper / lower case - treat 'X' and 'x' equally, and the same for 'O' and 'o'. If the count isn't the same, it should return False. If there are no Xs or Os in the string, it should also return True as zero and zero are equal.

Test it with 

1. "Lorem ipsum dolor sit amexut, consectetur adipiscing elit, sed do eiusmod 575 & tempor incididunt ut labore et dolore magna aliqua." (expect False)

2. "Ob ex enim ad minim vexiam, quis nestrud exercitation £96m ullamco ex laboris. Pax amici ex nisi ut aliquip exeat felix commodo consequat." (expect True)



Good luck.

Please upload your solutions to this Github repo. 