import random, os


def main():
    print_intro()
    word_list = get_word_list()
    random_word = random.choice(word_list)
    game_ended = False
    game_counter = 0
    previous_guesses = {}
    while not game_ended:
        print_previous(previous_guesses)
        guess_word = get_guess()
        result = game_loop(random_word, guess_word)
        previous_guesses[guess_word] = result
        cls()
        if result == "ooooo":
            print(f"You win! The word was {random_word}!")
            game_ended = True
        game_counter += 1
        if game_counter == 6:
            print(f"You lose! The word was {random_word}!")
            game_ended = True


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_guess():
    guess_word = input("Enter your guess: ").lower()
    return guess_word


def get_word_list():
    word_list = []
    with open("../wordlist.txt") as f:
        for line in f:
            word_list.append(line[:-1])

    return word_list


def print_previous(previous):
    for key, value in previous.items():
        print(f"{key}: {value}")


def game_loop(random_word: str, guess: str):
    if random_word == guess:
        return "ooooo"
    guess_result = ""
    for i, letter in enumerate(guess):
        if letter in random_word:
            if random_word[i] == guess[i]:
                guess_result += "o"
            else:
                guess_result += "-"
        else:
            guess_result += "x"

    return guess_result


def print_intro():
    print("Welcome to Pyrdle, Wordle in Python!")
    print("A random five letter word has been selected.")
    print("Guess what the word is!")
    print("A 'o' marks a correct letter, in the correct location.")
    print("A '-' marks a correct letter, in the wrong location.")
    print("A 'x' marks an incorrect letter.")


if __name__ == '__main__':
    main()
