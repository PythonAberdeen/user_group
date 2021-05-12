# Mostly from:
# https://gist.github.com/UmbreLu/b12c4fe79a54619804c928dc8224e014#file-answers_in_python-py-L429

def balanced(string): #returns true/false for balanced marks in string
	match = {')': '(', ']': '[', '}': '{'}
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


examples = ["({[]})", "aaaaaaa(a)aaaaaa", "abc(def{g}hi[jk]((()))l)m", "a(b", "([)]"]
[print(s, "=> ", balanced(s)) for s in examples]
