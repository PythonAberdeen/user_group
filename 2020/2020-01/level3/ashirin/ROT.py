import re
import random


def encrypt(sentence, number, divide_into):
    sentence_removed_chars_array = re.findall(r"[a-zA-Z']+", sentence)
    sentence_removed_chars = "".join(sentence_removed_chars_array).upper()
    encoded = ""

    for c in sentence_removed_chars:
        representation = (ord(c) + number - 65) % 26
        encoded += chr(representation + 65)

    with_spaces = "";
    for pos in range(len(encoded)):
        if pos == 0 or pos % divide_into != 0:
            with_spaces += encoded[pos]
        else:
            with_spaces += ' ' + encoded[pos]

    while (len(with_spaces)+1) % divide_into != 0:
        with_spaces += chr(random.randint(65, 90))

    return with_spaces


def decrypt(sentence, number):
    decoded = "";

    for c in sentence:
        if c != ' ':
            representation = (ord(c) - number - 65) % 26
            decoded += chr(representation + 65)
        else:
            decoded += ' '

    return decoded


encrypted = encrypt("Python Aberdeen!", 5, 4)
decrypted = decrypt(encrypted, 5)

print(encrypted)
print(decrypted)
