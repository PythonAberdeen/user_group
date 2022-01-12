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

If the player fails after six attempts the game should say that the word has not been guessed, show the correct word, and offer a new game with another random word. 

