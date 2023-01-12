import re
import requests
import collections

html = requests.get("https://www.lipsum.com/feed/html").text


def count_words(sentence):
    count = dict()
    sentence = re.sub(r"<[^>]*>", ' ', sentence)
    words = re.findall(r"[a-zA-Z']+", sentence)
    for element in words:
        word = element.lower()
        count[word] = count.get(word, 0) + 1
    return count


unordered_words = count_words(html)
ordered_words = collections.OrderedDict(sorted(unordered_words.items()))
print(ordered_words)
