import random
import click

from gallows import gallows

def pick_word(list="/usr/share/dict/words"):
    with open(list, encoding="utf-8", errors="ignore") as f:
        words = f.readlines()
    return random.choice(words).strip()

def blanks(word, guessed=""):
    l = ""
    for char in word:
        if char in guessed:
            l+=char
        else:
            l+="_"
    print(l)
    if "_" not in l:
        raise Exception("You win")

def draw_gallows(wrong=0):
    click.clear()
    print(gallows[wrong]) # should really check wrong is within gallows first...
    if wrong >= 6:
        raise Exception("You lose")
    

def get_guess():
    return input("Pick a letter:")
@click.command()
@click.option("--wlist", default="/usr/share/dict/words",
              help="Word list to pick from")
def main(wlist):
    word = pick_word(wlist)
    wrong = 0
    guessed = ""
    draw_gallows()
    blanks(word, guessed)
    try:
        while True:
            g = get_guess()
            if g not in word:
                wrong = wrong+1
            draw_gallows(wrong)
            guessed+=g
            blanks(word, guessed)
            print("Guesses so far: ", guessed)
    except Exception as e:
        print(word)
        print(str(e))

if __name__=="__main__":
    main()
