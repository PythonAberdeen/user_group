# Beginners' challenge July 2020

You have been given a list of names by your boss. 

["John", "Jane", "bob", "Susan", "Keith ", "Viktor", "Emmanuel", "Ahmed", "Billie", "June", "Fanny", "John ", "fred ", "Anna", "Shirley", "Son ny", "tina", " Ella", "Fred", "Edward"]

She says that she knows that there are some problems with the list.

She also gives you a [page of text](page.txt).

Your task is to check the page of text and to count how many times each of the names appears in the page and to print that out so that it appears as follows

> John: 1  
> Jane: 2  
> Bob: 0  

etc

She also says she thinks that the page has all names as lower case - but maybe not, she can't remember

Can you produce the printout as asked for in the next 90 minutes? 



## A suggested approach

If you need some hints you could work through it this way. 

1. Loop through the list of names 
 - check that there are no leading or trailing spaces. Get rid of them with the _strip()_ function. 
 - check that there are no spaces in the middle of words. Get rid of them with the _replace()_ function. You could combine these two steps as one.
 - check for duplicates of names. 
 - What about upper and lower case names - how would you check they are the same? Store them all as either upper or lower case. 

 2. Without reading the page of text, assume that names are a mix of cases. Treat them all the same (we suggest lower if that was what you did with your list). Iterate through the page of text a word at a time. Check if each word in your cleaned up name list is in the text. If it is, add one to the count for that name. 

 3. Print out your results, one name per line. Think about how you would format the output. You might want to use [f-strings](https://realpython.com/python-f-strings/). For example:
 > print(f"{name}: {name_count}") 
 or something like that. 

 Be prepared to share your results with the group at the end. 

