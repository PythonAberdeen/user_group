import random

wordlist = []
symbols = ['🟩', '🟨', '⬛']
with open ('wordlist.txt', 'r') as infile:
    for line in infile:
        wordlist.append(line.strip())

target_word = random.choice(wordlist).upper()
print (target_word)

turns = 0

def compare(guess, target):

while turns < 6:
    guess = input("Please guess a word: ").upper()
    print(f"Your guess was {guess}")

    if guess == target_word:
        Print ("Congratulations! You have guessed the word correctly! ")
    else:
        compare(guess, target_word)
    turns += 1