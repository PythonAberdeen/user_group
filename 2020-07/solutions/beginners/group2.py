import sys
from collections import namedtuple

names = ["John", "Jane", "bob", "Susan", "Keith ",
         "Viktor", "Emmanuel", "Ahmed", "Billie",
         "June", "Fanny", "John ", "fred ", "Anna",
         "Shirley", "Son ny", "tina", " Ella", "Fred",
         "Edward"]
clean_names = list(set([x.replace(" ","").lower()
                        for x in names]))
if len(sys.argv) < 2:
    filename = "page.txt"
else:
    filename = sys.argv[1]
with open(filename) as f:
    text = f.read()
words = text.lower().replace(".","").split()

Result = namedtuple("Result", "name count")
counts = [Result(name=n.title(), count=words.count(n))
          for n in clean_names]

for m, k, r in [("Sorted by count", lambda t: t.count, True),
                ("Sorted by name", lambda t: t.name, False)]:
    sorted_counts = sorted(counts, key=k, reverse=r)
    print(m)
    for c in sorted_counts:
        print(c.name, ": ", c.count)
    print()

