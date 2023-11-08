# Aberdeen Python User Group - November 2023
# Beginner Coding Challenge
# Dr Lee A. Christie
#
# Add type hints to the arguments and return values of
# these functions and run mypy to check that the examples
# of type errors are detected by mypy without
# running the code.
#
# Do not run the Python code, only run mypy to check types.


# takes two int arguments and retunrs the largest int
def max_integer(a, b):
    if a >= b:
        return a
    else:
        return b


# correct - mypy should not give type checking error
print('the max of 1 and 2 is', max_integer(1, 2))

# incorrect - mypy SHOULD give type checking error
print('the max of 1 and "x" is', max_integer(1, "x"))


# accepts an int or str value expecting 42 or "42"
# and prints a message
# does not return anything
def print_if_42(value):
    if int(value) == 42:
        print('yay!')
    else:
        print('aww :(')


# correct - mypy should not give type checking error
print_if_42(1)
print_if_42(42)

# correct - mypy should not give type checking error
print_if_42("foo")
print_if_42("42")

# incorrect - mypy SHOULD give type checking error
print_if_42([42])


# accepts a list of ints
# takes the first two unique values and returns them as a set
def first_two_unique_as_a_set(values):
    result = set()
    for value in values:
        result.add(value)
        if len(result) == 2:
            return result
    return result


# correct - mypy should not give type checking error
print(first_two_unique_as_a_set([5, 6, 7]))

# correct - mypy should not give type checking error
print(first_two_unique_as_a_set([1, 1, 2, 3, 4, 5]))

# incorrect - mypy SHOULD give type checking error
print(first_two_unique_as_a_set(["foo"]))


# accepts a list of str or None
# counts how many Nones
# return an int
def now_many_nones(values):
    result = 0
    for value in values:
        if value is None:
            result += 1
    return result


# correct - mypy should not give type checking error
print(now_many_nones(["foo", "bar", "baz"]))

# correct - mypy should not give type checking error
print(now_many_nones([None, None, None, None]))

# incorrect - mypy SHOULD give type checking error
print(now_many_nones([1]))
