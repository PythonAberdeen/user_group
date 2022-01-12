# APUG January 2022 Intermediate Challenge

Today we are going to build a text-based, Python version of [Wordle](https://www.powerlanguage.co.uk/wordle/) - let's call it Pyrdle. 

## Game play

The person playing the game is presented with a randomly chosen word from a list. 

They have six attempts to guess the word correctly. 

On each attempt they are presented with symbols to indicate their success. 

<pre>
	* = a letter in the correct place
	+ = a correct letter in the wrong place
	- = a wrong letter
</pre>

Suppose the word to be guessed is 'paint'

The player enters 'plant'

The display should be as follows

<pre>
*-+**
</pre>

Play continues for 6 rounds, or until the player has guessed correctly. 

If the player guesses correctly on any round a suitable congratulatory message should be shown. 

If the player fails after six attempts the game should say that the word has not been guessed, and show the correct word. 

In either case the game should then offer a new game with another random word. 

## Things to consider

# We have provided a lower-case [list of 500 words](https://github.com/PythonAberdeen/user_group/blob/master/2022-01/intermediate/wordlist.txt) but you can use your own. Is lower-case the best for display and input-matching? 
# How do you count the six attempts? How do you end before those are up if the player guesses correctly

## Enhancements 

# Remembering previous attempts is difficult. While the game is not ended, can you show previous attempts and their symbols? 
# Having a keyboard display with letters which elimited marked in some way might be helpful to the players 


Have fun. 

Remember to upload your solutions to Github when you complete them. 




