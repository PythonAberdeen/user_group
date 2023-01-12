#%% Option 1: Do the dictionary yourself

# a = {'Stephen King':'21 September 1947',
#      'Roger Federer':'8 May 1981',
#      'Lewis Hamilton':'7 May 1985',
#      'Lewis Capaldi ':'7 October 1996',
#      'Dame Judy Dench':'9 December 1934',
#      'Baroness Susan Greenfield':'1 October 1950'}

#%% Option 2: Import from a csv file

import csv

reader = csv.reader(open('birthdays.csv','r'))
a = {}
for line in reader:
    a[line[0]]=line[1]
    

#%% Main code (missing many things, just the basic stuff!)

print('We know the birthdates of...')
for k,v in a.items():
    print(k)
print("Which person's birthday would you like to know?")
b=input('>>')

try:
    print(b+' was born on '+a[b])
except:
    print("An exception occurred") 
    
    