#%% load packages
import re

#%% Part 1
on_power=[]
on = 0
off_power=[]
off = 0
f = open("power.txt", "r")
for x in f:
  # find the amps measurement
  digit = re.search(r'\d+.\d+', x)
  # convert it into numbers
  digit = float(digit.group())
  # add it to on or off depending of the value
  if digit > 1:
      on = on + digit
      # add the text line to a list
      on_power.append(x)
  else:
      off = off + digit
      # add the text line to a list
      off_power.append(x)
# Calculate the average
on_average = on/len(on_power)
off_average = off/len(off_power)
# Difference between the two is the value
current_draw = on_average - off_average

# close file
f.close()

#%% Part 2
import datetime

# load files
list_logs= ["20210105-test.log", 
            "20210106-test.log"]
for log in list_logs:
    f = open(log, "r")
    # work with the log
    for x in f:
        # if the line has a date
        if ":" in x:
            print(datetime.datetime.strptime(x.strip(), "%a %b %d %H:%M:%S %Y"))

