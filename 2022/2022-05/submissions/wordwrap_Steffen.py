"""
Write a function wordwrap which, given an input string and line length, outputs the text in the form of a list of strings that length, for example:

>>> wordwrap('The quick brown fox jumps over the lazy dog', 15)
['The quick brown',
 ' fox jumps over',
 ' the lazy dog  ']

If there is a word which won't fit on a line at all, break it with a hyphen. Remember to count the hyphen towards the line length!

>>> wordwrap('Harry cast Expelliarmus to disarm Voldemort', 10)
['Harry cast',
 'Expelliar-',
 'mus to    ',
 'disarm    ',
 'Voldemort ']
"""

# this function does literally what was asked in the README, means it splits the whole string after {length} items.
# but this is not what was asked in the original example by Robert Martin.
def wordwrap(stw, length):
    count = 0
    split_string = []
    while count < len(stw):
#        print("step 1")
        if count < (len(stw) - length):
#            print("step 2", count, len(stw))
            if stw[(count + length)] != " " and (stw[(count + length - 1)] != " " or stw[(count + length +1)] != " "):
#                print("step 3-1")
                split_string.append(stw[count:(count + length - 1)] + "-")
                count += length - 1
#                print("1", count, split_string)
            else:
#                print("step 3-2")
                split_string.append(stw[count:(count + length)])
                count += length
#                print("2", count, split_string)
        else:
            split_string.append(stw[count:(count + length)])
            count = len(stw)

    print(split_string)

string_to_wrap1 = "the quick brown fox jumps overr the lazy dog"
wrap_after1 = 15

string_to_wrap2 = "Harry cast Expelliarmus to disarm Voldemort"
wrap_after2 = 10

wordwrap(string_to_wrap1, wrap_after1)
wordwrap(string_to_wrap2, wrap_after2)
