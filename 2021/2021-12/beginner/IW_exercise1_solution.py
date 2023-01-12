increase_count = 0
current_pos = 0
with open ('input.txt', 'r') as infile:
	for line in infile:
		current_val =  int((line.strip()))
		if current_pos > 0:
			if current_val > old_val : 
				increase_count += 1
		old_val = current_val
		current_pos +=1

print (increase_count)
