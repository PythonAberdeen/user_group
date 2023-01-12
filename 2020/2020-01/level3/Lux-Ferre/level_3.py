import re, collections
from os import path

def main():

    menu_choice = input("What would you like to do? ")[0].lower()

    if menu_choice == "e":
        input_string = input("What would you like to encrypt? ").lower()
        n = int(input("Which ROT cypher do you wish to use? [0-26] "))
        s = int(input("How many characters would you like per slice? "))
        encrypted_string = encrypt(input_string, n)
        sliced_string = slicer(encrypted_string, s)
        output_string = sliced_string
    elif menu_choice == "1":
        input_string = load_data(1).lower()
        n = int(input("Which ROT cypher do you wish to use? [0-26] "))
        output_string = decrypt(input_string, n)
    elif menu_choice == "2":
        input_string = load_data(2).lower()
        stripped_string = re.sub(" ", '', input_string)
        most_common = collections.Counter(stripped_string).most_common(1)[0][0]
        common_num = ord(most_common)
        ROT_number = abs(common_num - 101)
        output_string = decrypt(input_string, ROT_number)

    elif menu_choice == "d":
        input_string = input("What would you like to decrypt? ").lower()
        n = int(input("Which ROT cypher do you wish to use? [0-26] "))
        output_string = decrypt(input_string, n)

    print(output_string)


def encrypt(input_string, n):
    stripped_string = re.sub("[^a-z]+", '', input_string)
    output_string = ""

    for e in stripped_string:
        char_num = ord(e)
        new_num = char_num + n
        if new_num > 122:
            new_num = new_num - 26
        new_char = chr(new_num)
        output_string = output_string + new_char

    return output_string

def slicer(input_string, n):
    i = 0
    output_string = ""
    for e in input_string:
        i = i + 1
        output_string = output_string + e
        if i == n:
            i = 0
            output_string = output_string + " "
    return output_string

def decrypt(input_string, n):
    return encrypt(input_string.strip(), 26-n)

def load_data(n):
    filename = path.abspath('./CYPHER{}.txt').format(n)
    return_string = ""

    if path.exists(filename):
        with open(filename, 'r') as raw_data:
            for line in raw_data:
                return_string = return_string + line
    return return_string

if __name__ == '__main__':
    main()