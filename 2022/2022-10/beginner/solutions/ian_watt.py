#exercise 1
def count_vowels(instring):
	"""
	A fuction which takes a string input, counts the vowels and returns an integer of that count
	"""
	vowels = ['a','e','i','o','u']
	
	cv = 0
	for letter in instring:
		if letter.lower() in vowels: # used lower built-in function to test for match to lowercase vowels
			cv+=1 
	return cv 

#test1 

count = count_vowels ("Aakshdieuybadc")
print(count)

#test2 
count = count_vowels ("nymphs")
print(count)


#Exercise 2

def x_and_o(instring):
	"""
	A fuction which takes a string input, checks the count of Xs and Os, compares these and returns whether True (they are the sane) or False
	"""
	exes = 0
	os = 0
	for letter in instring:
		if letter.lower() == 'x':
			exes += 1
		if letter.lower() == 'o':
			os +=1
	if exes == os:
		return True
	else:
		return False


xotest = x_and_o("Lorem ipsum dolor sit amexut, consectetur adipiscing elit, sed do eiusmod 575 & tempor incididunt ut labore et dolore magna aliqua." )
print (xotest)
xotest = x_and_o("Ob ex enim ad minim vexiam, quis nestrud exercitation £96m ullamco ex laboris. Pax amici ex nisi ut aliquip exeat felix commodo consequat." )
print (xotest)
