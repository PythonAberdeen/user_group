## A suggested approach

If you need some hints you could work through it this way. 

1. Create a Python list from the names
 - Loop through the list of names 
 - Check that there are no leading or trailing spaces. Get rid of them with the _strip()_ function. 
 - Check that there are no spaces in the middle of words. Get rid of them with the _replace()_ function. Could you combine these two steps as one?
 - Check for duplicates of names. What about upper and lower case names? How would you check they are the same? Hint: store them all as either upper or lower case. 

 2. Load your page of text into a string. 
  - Don't try to physically read it yourself. It could be book length. 
  - Assume that names are a mix of cases. Treat them all the same (we suggest lower if that was what you did with your list) and then you are comparing like with like. 
  - Iterate through the page of text a word at a time. 
  - Check if each word in your cleaned up name list is in the text. If it is, add one to the count for that name. Do you need to store that count or just print it out?

 3. Print out your results, one name per line. 
  - Think about how you would format the output. 
  - You might want to use [f-strings](https://realpython.com/python-f-strings/). For example:
 > print(f"{name}: {name_count}")  
 
 or something like that. 

 4. For a more elegant solution - with sorted results think about data structures. 
  - would a dictionary work? It holds key:value pairs. 
  - how would you sort the dictionary by keys?
  - how would you sort the dictionary by values?
  - and how do you iterate through a dictionary to print out the results? 

