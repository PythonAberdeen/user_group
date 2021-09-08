import pytest

  # To calculate number words
Powers = [("hundred", 2), ("thousand", 3), ("million", 6), ("billion", 9), ("trillion", 12)]
Tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
Teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
         "seventeen", "eighteen", "nineteen"]
Digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def wordnumber(text):
    ## Change number words to numbers
    words = [w for w in text.split(" ") if w]
    ns = ""
    mode = ""
    mode_num = 0
    mode_index = 0
    charge = 0
    last_num = ""

    def zeropad(diff): 
        zeroes = ""
        for _ in range(diff):
            zeroes += "0"
        return zeroes
  
    def checkdiff(i, ns):
        diff = mode_num - charge
        if diff > 0:
            if i > 0:
                if i + 1 < len(words):
                    if mode_index - 1 >= 0:
                        p2 = Powers[mode_index - 1]
                        for i2 in range(i, len(words)):
                            word = words[i2]
                            if word == p2[0]:
                                return ns
            zeroes = zeropad(diff)
            if charge > 0:
                ns = ns[:-1*len(last_num)] + zeroes + last_num
            else:
                ns += zeroes
        return ns

    for i, word in enumerate(words):
        if word == "point":
            ns += "."
            continue
        for pi, p in enumerate(Powers):
            if p[0] == word:
                ns = checkdiff(i, ns)
                mode = p[0]
                mode_num = p[1]
                mode_index = pi
                charge = 0
                break
      
        last_num = ""
      
        if word in Digits:
            last_num = str(Digits.index(word))
        elif word in Teens:
            last_num = str(Teens.index(word) + 10)
        elif "-" in word:
            split = word.split("-")
            last_num = str(Tens.index(split[0]) + 2) + str(Digits.index(split[1]))
      
        charge += len(last_num)
        if last_num:
            # print(f"{ns=} {last_num=} {word=}")
            ns += last_num
  
    ns = checkdiff(0, ns)

    if words[0] == "minus":
        ns = "-" + ns

    return float(ns)


test_data = [
    ("four", 4.0),
    ("zero",  0),
    ("fifty", 50),
    ("fifty-two", 52),
    ("six hundred three", 603.0),
    ("six hundred three million",  603000000.0),
    ("six hundred three million and four", 603000004.0),
    ("zero point three three", 0.33),
    ("six hundred three million and four point three three", 603000004.33),
    # ^^ producing 6034.30003
    ("six million three hundred ten thousand six hundred thirty-two", 6310632.0),
    ("minus four thousand two",  -4002.0),
    ("thirty-three point three", 33.3),
    ("thirty-three point five hundred thirty-two thousand eleven", 33.532011 ),
    # ^^ I hate this, but people do seem to write numbers like this...
    ("twelve thousand and two point three", 12002.3),
    ("thirty million", 3e7),
    ("thirty million and four", 3e7+4),
    
]

@pytest.mark.parametrize('words, val', test_data)
def test_wordnumber(words, val):
    assert wordnumber(words) == val

