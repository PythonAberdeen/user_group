def balanced(string):
    pairs = {'(' : ')', '[' : ']', '{' : '}'}
    if string is None:
        return True
    if string == '':
        return True
    if string[0] in pairs.values():
        return False
    if string[0] in pairs.keys():
        open_bracket = string[0]
        close_bracket = pairs[open_bracket]
        if len(string) == 1:
            return False
        if string[-1] in pairs.keys():
            return False
        if string[-1] == close_bracket:
            return balanced(string[1:-1])
        if string[-1] in pairs.values():
            for i in range(1, len(string)):
                left = string[:i]
                right = string[i:]
                if balanced(left) and balanced(right):
                    return True
            return False
        return balanced(string[:-1])
    return balanced(string[1:])
  
print(balanced("({[]})"))                    # True
print(balanced("abc(def{g}hi[jk]((()))l)m")) # True
print(balanced("a(b"))                       # False
print(balanced("([)]"))                      # False
