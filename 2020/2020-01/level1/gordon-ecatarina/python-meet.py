
userInput = input('Please enter a sentence: ')

vowels = ['A','a', 'E', 'e', 'I', 'i', 'O', 'o', 'U' 'u']

eachWord = userInput.split()
returnString = ''

for word in eachWord:
    if word[0] in vowels:
        result = word + '-way '
    else:
        result = word[1:] + '-' + word[0] + 'ay '
    returnString += result
print(returnString)
