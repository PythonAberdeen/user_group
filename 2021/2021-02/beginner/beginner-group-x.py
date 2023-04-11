#Typed by Emmanuel, with input from one of the beginner rooms

#Program to print out a statement and check acuracy
from datetime import datetime

def check_statement(statement):
    target = 'She sells seashells by the seashore'
    var1 = 0
    for i, c in enumerate(target):
        if i<len(statement):
            d = statement[i]
        else :
            d = None
        if c==d:
            var1+=1   
    return 100*var1/len(target)

keep_going = True
while keep_going: 
    print("She sells seashells by the seashore")
    start = datetime.now()
    statement = input(">")
    end = datetime.now()
    acuracy = check_statement(statement)
    print(round(acuracy,1), '%')
    time_taken = end - start
    print('Time taken by user: ',time_taken) 
    if acuracy == 100:
        keep_going = False
