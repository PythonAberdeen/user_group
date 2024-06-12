# Challenge 1
'''

for n in range(1,101):

    if n % 15 == 0:
        print ("Fizz Buzz")
    elif n % 5 == 0:
        print ("Buzz")
    elif n % 3 == 0:
        print ("Fizz")
    else:
        print(n)
'''
# Challenge 2
'''
import re

test_string = input("input a string to test > ")
test_lower = test_string.lower()
test_lower = re.sub('[^0-9a-zA-Z]+', '', test_lower)
reversed = test_lower[::-1]

if test_lower == reversed:
    print ("I'm a palindrome")
else:
    print ("I'm not a palindrome")
'''

#Challenge 3
print("Enter a list of whole numbers, one at a time.")
print("Enter 'Z' to finish input")

finish = False
input_list = []
while not finish:
    number = input(">>")
    if number == "Z" or number == "z":
        finish = True
    else:
        input_list.append(int(number))
#print(input_list)
total = 0
for n in input_list:
    if n % 2 == 0:
        total = total+n
print(total)

