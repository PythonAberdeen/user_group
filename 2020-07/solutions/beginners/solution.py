#!/usr/bin/env python3

raw_names = ["John", "Jane", "bob", "Susan", "Keith ", "Viktor", "Emmanuel", "Ahmed", "Billie", "June", "Fanny",
			 "John ", "fred ", "Anna", "Shirley", "Son ny", "tina", " Ella", "Fred", "Edward"]

clean_names = []

for name in raw_names:
	name = name.strip().replace(" ", "").lower()
	clean_names.append(name)

clean_names = list(set(clean_names))  # a neat trick turning a list into a set into a list removes all duplicates

# get our page of text and store it in a string
with open('page.txt', 'r') as file:
	data_str = file.read().replace('\n', '')

# use the string.count() method
print("All names appearing more than once")

for word in clean_names:
	wc = data_str.count(word)
	if wc > 0:
		print(f"{word.capitalize()}: {wc}")

# Enhanced methods
#===================

#use a dictionary
print()
print("Only names occurring one or more times, sorted by name")
name_count_dict = {}

for word in clean_names:
	wc = data_str.count(word)
	name_count_dict[word] = wc

for key in sorted(name_count_dict.keys()):
	if name_count_dict[key] != 0:
		print(f"{key.capitalize()}: {name_count_dict[key]}")

# use the dictionary but sort by count
sort_by_numbers = sorted(name_count_dict.items(), key=lambda x: x[1], reverse=True)
print()
print("Only names occurring one or more times, sorted by count")
for i in sort_by_numbers:
	if i[1] > 0:
		print(f"{i[0].capitalize()}: {i[1]}")
