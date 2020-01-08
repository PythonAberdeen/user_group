alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
alphabet_len = len(alphabet)


def cipher(text, number, chunk):
    new_text = ""
    i = 0;
    for letter in text:
        try:
            position = alphabet.index(letter.capitalize())
            new_position = position + number
        except Exception:
            continue
        if new_position > alphabet_len:
            new_position = number - (alphabet_len - position)
        new_text += alphabet[new_position]
        i += 1
        if i == 4:
            new_text += ' '
            i = 0
    return new_text


def decipher(text, number):
    new_text = ""
    for letter in text:
        if letter == ' ':
            new_text += letter
            continue
        try:
            position = alphabet.index(letter)
            new_position = position - number
        except Exception:
            continue
        if position - number < 0:
            new_position = alphabet_len - (number - position)
        new_text += alphabet[new_position]
    return new_text


print(cipher('Python Aberdeen!', 5, 4))
print(decipher('UDYM TSFG JWIJ JSXI', 5))
