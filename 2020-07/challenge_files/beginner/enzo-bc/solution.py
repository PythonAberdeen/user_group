original_list = ["John", "Jane", "bob", "Susan", "Keith ", "Viktor", "Emmanuel", "Ahmed", "Billie",
                 "June", "Fanny", "John ", "fred ", "Anna", "Shirley", "Son ny", "tina", " Ella",
                 "Fred", "Edward"]
"""
dictionary comprehension is used to achieve distinct name: number of occurrences structure
"""
names = {x: 0 for x in [item.lower().replace(" ", "") for item in original_list]}

"""
with statement is used instead of try finally to make code cleaner
"""
with open('../page.txt') as reader:
    file_content = reader.read()

"""
update each dictionary key with number of occurrences in file
"""
names.update((key, file_content.count(key.lower())) for key in names.keys())

"""
sorted changes dictionary to list of tuples.
key=lambda x: x[1] picks dictionary value as a key to sort
"""
results = sorted(names.items(), key=lambda x: x[1], reverse=True)

for item in results:
    print(f"{item[0].capitalize()}: {item[1]}")

