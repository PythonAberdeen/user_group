from textwrap import wrap

def prompt_for_word(prompt):
    answer = ''
    show_error = False
    while not answer:
        if show_error:
            print('Try again!')
        show_error = True
        answer = input(prompt + ':')
    return answer

with open('python.txt', 'r') as file:
    text = file.read().replace('\n', '')

while '[' in text:

    # get the prompt
    start = text.index('[')
    end = text.index(']')
    prompt = text[start+1:end]

    # prompt the user
    answer = prompt_for_word(prompt)

    # update the text
    left = text[:start]
    right = text[end+1:]
    text = left + answer + right

# print the final mad lib
print()
for line in wrap(text, 80):
    print(line)
