import pytest

def numberword(num):
    """
    Change number to words
    """
    if num == 4:
        return "four"
    return "zero"

def wordnumber(text):
    """
    Change number words to numbers
    """
    if text == "four":
        return 4
    return 0


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
    ("six million three hundred ten thousand six hundred thirty-two", 6310632.0),
    ("minus four thousand two",  -4002.0),
    ("thirty-three point three", 33.3),
    ("twelve thousand and two point three", 12002.3),
    ("thirty million", 3e7),
    ("thirty million and four", 3e7+4),
    
]

bad_test_data = [
    ("thirty-three point five hundred thirty-two thousand eleven", 33.532011 ),
    # ^^ I hate this, there *aren't* thousands after the decimal point,
    # but people do seem to write numbers like this so should support
    # it in parsing words.
    # Don't want it to be produced from numberword()
]

@pytest.mark.parametrize('words, val', test_data)
def test_numberword(words, val):
    assert numberword(val) == words

@pytest.mark.parametrize('words, val', test_data+bad_test_data)
def test_wordnumber(words, val):
    assert wordnumber(words) == val

