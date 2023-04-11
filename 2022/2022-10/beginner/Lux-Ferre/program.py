def count_vowels(word: str) -> int:
    vowels = "aeiou"
    vowel_count = 0

    for letter in word:
        if letter in vowels:
            vowel_count += 1

    return vowel_count


def x_or_o(word: str) -> bool:
    word = word.lower()
    x_count = 0
    o_count = 0

    for letter in word:
        if letter == "x":
            x_count += 1
        elif letter == "o":
            o_count += 1

    if x_count == o_count:
        return True
    else:
        return False


def main():
    print(x_or_o(""))


if __name__ == "__main__":
    main()
