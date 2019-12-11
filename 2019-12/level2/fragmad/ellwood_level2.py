
def count_words(input_string):
    result = {}
    string_list = input_string.split(" ")
    string_set = set(string_list)

    for word in string_set:
        result[word] = 0

        for token in string_list:
            if word == token:
                result[word] = result[word] + 1
    return result

def insensitive_count_words(input_string):
    result = {}
    input_string = input_string.lower()
    string_list = input_string.split(" ")
    string_set = set(string_list)

    for word in string_set:
        result[word] = 0

        for token in string_list:
            if word == token:
                result[word] = result[word] + 1
    return result

if __name__ == '__main__':
    example = "fun fun what fun is python"
    print(count_words(example))
    print(count_words("Don't stop coding in Python"))
    print(insensitive_count_words("Don't stop coding in Python"))
    print(insensitive_count_words(example))
    print(count_words("abc ABC"))
    print(insensitive_count_words("abc ABC"))

