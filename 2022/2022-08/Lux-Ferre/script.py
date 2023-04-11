file_path = "/storage/emulated/0/git-projects/user_group/2022-08/data/100words.txt"

with open(file_path) as file:
	words = {line.strip() for line in file} 

words = ["act", "actor", "acting", "actors"]
words_dict = dict()

for word in words:
		words_dict["".join(sorted(set(word)))] = word
		
		
def clean_word_list():
	remove_list = list()
	
	for key in words_dict:
		i = 0
		for key2 in words_dict:
			if set(key).issubset(set(key2)):
				i += 1
				if i > 1:
					remove_list.append(key)
					break
	
	for removed in remove_list:
		del words_dict[removed]
