import csv
import random

# Load data from external file
filename = "birthdays.csv"
birthdays = {}
reader = csv.reader(open(filename,'r'))
for line in reader:
    birthdays[line[0]]=line[1]

responses = [" was born on", " has a birthday on", "'s birthday falls on", " arrived in this world on"]  #we can randomly choose a phrase below
# Start interaction
print ("Welcome to the birthday look-up service")
print ("\nwe know the birthdays of ")

for key in birthdays:
    print(key)
print("\n======================\n")
print("Which person's birthday would you like to know?")

# Create an infinite loop until we choose to BREAK out of it
repeat = ""
while True:
    print("Type 'Stop' to finish.\n")
    in_name = input(f"Enter a {repeat}name: ").lower() #convert input to lower case
    if in_name == "stop":
        break
    found = False

    for key, val in birthdays.items():
        if in_name == key.lower(): #comparing lower case with lower case
            middle = random.choice(responses)
            print (f"{key}{middle} {val}.")
            found = True
            repeat = "another " # we can insert "another" into our prompt
            print("\nWhy not try again?")
    if not found:
        print ("Sorry I couldn't find that name")

