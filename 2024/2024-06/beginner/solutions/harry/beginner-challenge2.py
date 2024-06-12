
def isPalindrome(input):
    input = input.lower().replace(' ', '')
    c = len(input) - 1
    for i in range(0, len(input)):
        if input[i] != input[c]:
            return False
        c -= 1
    return True


print(isPalindrome("Madam"))
print(isPalindrome("Goody"))
print(isPalindrome("I am Mai"))
