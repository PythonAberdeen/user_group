# Challenge 1
'''
import re
print("Input two strings to see if they are anagams")
first_string = input("Input first string > ")
second_string = input("Input second strng >")


first_lower = first_string.lower()
second_lower = second_string.lower()


first_lower = re.sub('[^0-9a-zA-Z]+', '', first_lower)
second_lower = re.sub('[^0-9a-zA-Z]+', '', second_lower)

first_sorted = ''.join(sorted(first_lower))
second_sorted = ''.join(sorted(second_lower))


if first_sorted == second_sorted:
    print ("Your words were anagrams")
else:
    print ("They were not anagrams")
'''
# Challenge 2
# Answer provided by ChatGPT4.0
def prime_factors(n):
    factors = []

    # Check for the number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # n must be odd at this point, so we can skip even numbers
    for i in range(3, int(n ** 0.5) + 1, 2):
        # While i divides n, append i and divide n
        while n % i == 0:
            factors.append(i)
            n = n // i

    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)

    return factors


# Example usage
n = 56
print(f"Prime factors of {n}: {prime_factors(n)}")

n = 45
print(f"Prime factors of {n}: {prime_factors(n)}")


