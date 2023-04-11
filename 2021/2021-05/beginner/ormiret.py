# Mostly from:
# https://gist.github.com/UmbreLu/b12c4fe79a54619804c928dc8224e014#file-answers_in_python-py-L429

match = {')': '(', ']': '[', '}': '{'}

def balanced(string): #returns true/false for balanced marks in string
    last_open = '@'
    for pos, char in enumerate(string):
            if char in '([{':
                    last_open, last_pos = char, pos
            if char in ')]}':
                    if last_open != match[char]:
                            return False
                    else:
                            return balanced(string[:last_pos] + string[pos + 1:])
    return last_open == '@'

# Alternative approach that keeps list of opening brackets seen rather than recursing:
def balanced_stack(string):
    brackets = []
    for char in string:
        if char in match.values():
            brackets.append(char)
        if char in match.keys():
            if brackets and brackets[-1] == match[char]:
                brackets.pop()
            else:
                return False
    return brackets == []
            
    
examples = ["({[]})", "aaaaaaa(a)aaaaaa", "abc(def{g}hi[jk]((()))l)m", "a(b", "([)]", "("]

print("Recursive version:")
[print(s, "=> ", balanced(s)) for s in examples]

print("\nStack version:")
[print(s, "=> ", balanced_stack(s)) for s in examples]
