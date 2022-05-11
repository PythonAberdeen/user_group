def test_suite(input_string: str, max_length: int):
    string_list = wordwrap(input_string, max_length)
    print(f" Max Test: {test_max_length(string_list, max_length)}")
    print(f" Min Test: {test_min_length(string_list, max_length)}")


def test_max_length(string_list: list, max_length: int):
    for line in string_list:
        if len(line) > max_length:
            return False

    return True


def test_min_length(string_list: list, max_length: int):
    for line in string_list:
        if len(line) < max_length:
            return False

    return True


def wordwrap(input_string: str, max_length: int) -> list:
    string_list = []
    word_list = input_string.split(" ")
    current_line = word_list[0]
    word_list.pop(0)

    for word in word_list:
        while len(word) > max_length:
            cropped_word = word[:max_length-1] + "-"
            string_list.append(current_line)
            string_list.append(cropped_word)
            word = word[max_length - 1:]
            current_line = ""

        new_line = current_line + " " + word
        if len(new_line) <= max_length:
            current_line = new_line
        else:
            current_line = f"{current_line: <{max_length}}"
            string_list.append(current_line)
            current_line = word

    current_line = f"{current_line: <{max_length}}"
    string_list.append(current_line)

    return string_list


if __name__ == "__main__":
    input_string = "The quick brown fox jumps over the lazy dog"
    # input_string = "Harry cast Expelliarmus to disarm Voldemort"
    max_length = 10

    print(wordwrap(input_string, max_length))
    test_suite(input_string, max_length)
