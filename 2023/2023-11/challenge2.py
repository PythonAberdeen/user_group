# Aberdeen Python User Group - November 2023
# Intermediate Coding Challenge
# Dr Lee A. Christie
#
# This code contains some bugs which can be revealed by adding
# the appropriate type hints, then running through mypy.
# Your task is to use type hints to reveal the bugs!


# takes a string and parses it to an int or float
# if it can't be parsed, returns None
def parse_to_number(s):

    # try to parse to an int, e.g. "42" -> 42
    try:
        return int(s)
    except ValueError:
        pass

    # try to parse to float, e.g. "3.14" -> 3.14
    try:
        return float(s)
    except ValueError:
        pass

    # can't be parsed, return None
    return None


# given a (space separated) string
# e.g. "foo 10 hello 3.14 42"
# gets the numbers ignoring non-numbers
# e.g. [10, 3.14, 42]
def get_numbers_from_string(s):

    # split the string
    tokens = s.split(' ')
    numbers = []

    # get each number in the string
    for t in tokens:
        numbers.append(parse_to_number(t))

    # return the numbers
    return numbers


# given a non-empty collection of numbers,
# returns the median
def find_median(numbers):

    # check for empty collection
    if not numbers:
        raise ValueError('numbers is empty')

    # convert to a sorted list
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)

    # even-length list
    if length % 2 == 0:
        middle_right = length // 2
        middle_left = middle_right - 1
        left = sorted_numbers[middle_left]
        right = sorted_numbers[middle_right]
        return (left + right) / 2

    # odd-length list
    middle = length // 2
    return sorted_numbers[middle]


def main():
    s = 'Python 3.12 was released on 2 October 2023'
    numbers = get_numbers_from_string(s)
    median = find_median(numbers)
    print(f'The median is {median}')


if __name__ == '__main__':
    main()
