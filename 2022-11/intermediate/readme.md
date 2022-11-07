# Intermediate Challenge 09 Nov 2022
Set by [Ian Watt](https://github.com/watty62) - Licence [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/)

## Scenario
You have been given a [log of client data](fake_client_data.csv): note the data in this text file was generated using [Mockaroo](https://mockaroo.com) and contains _only_ machine-generated fake data. 

You have been asked to write a Python script to ingest this data and to analyse it to present the following report:

* The number of each type of top-level domain used in email addresses (.com, .org etc)
* The number of users for each full domain name (eg. dailymail.co.uk)
* The number of instances of each first part of postcodes where there are two parts which should either be separated by a space or dash (eg. 123 456 or 9997-8088 which would yeild 123 and 9997 respectively). All other types of data should be disregarded.
* What have we more of? Male or female users? 

## Constraints
While there are several approaches that could be used (aren't there always in Python), in this case you should primarly use Regular expressions to match patterns, extract parts of strings (think about capture groups) or sequences of characters. 

## Caution

Your manager says that you might want to note that the data quality was not well checked before it was written to the Customer Service Database. In the past they found that:

* Some people were very guarded about how they entered their email addresses. 

* Some had capslock on or couldn't find their caps key. 

* Some customers weren't sure about the separator character in their postcode. Or how many to use. 

* Oh, and the CSV export didn't insert commas in the records. 
