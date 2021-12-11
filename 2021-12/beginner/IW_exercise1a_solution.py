depth_values = []
old_val = 30000 #bigger than highest value in file
increase_count = 0

with open ('input.txt', 'r') as infile:
	for line in infile:
		depth_values.append(int(line.strip()))

for x in range (0,1998):
	current_val = sum([depth_values[x], depth_values[x+1], depth_values[x+2]])
	if current_val > old_val:
		increase_count += 1
	old_val	 = current_val

print (increase_count)