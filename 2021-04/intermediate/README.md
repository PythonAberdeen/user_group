# PyXLL Challenge April 2021

[PyXLL](https://www.pyxll.com) is an Excel add-in for calling Python functions from Excel.

In this challenge you will use PyXLL to load a list of Formula One drivers and statistics
from Wikipedia into Excel and perform some data analysis.

## Prerequisites

For this challenge you will need

- A Windows PC
- Microsoft Excel
- A Python environment that is the same 'bitness' as your Excel version
- The PyXLL Excel add-in

To check if you have 64 or 32 bit Excel installed see this
[FAQ article](https://support.pyxll.com/hc/en-gb/articles/360036821613-Do-I-have-32-bit-or-64-bit-Excel-).
You will need to have a matching 32 bit or 64 bit version of Python available.

Once you have sorted out your Excel and Python environments you can install the PyXLL add-in.
This is the first part of the challenge! Follow the [installation instructions on the PyXLL
website](https://www.pyxll.com/docs/userguide/installation/index.html) to install the PyXLL add-in.

## The Challenge

Make an Excel spreadsheet that an Excel user can use to answer the following questions
about Formula One Drivers.

- What are the top 10 drivers by race wins of all time?
- Which driver has the lowest ratio of race entries to race starts?
- What are the top 5 mean race wins by race starts by nationality?

## Tips

- Start by writing a Python function that loads the Formula One data and parses it into a
  pandas DataFrame.
- Write the code to do the first challenge in Python first before thinking about how to do it in Excel. 
- Use PyXLL's [@xl_func](https://www.pyxll.com/docs/userguide/udfs/introduction.html) decorator to expose
  function to Excel.
- You can pass Python objects between functions in Excel (see [https://www.pyxll.com/docs/userguide/udfs/cached-objects.html]())
  without having to expand everything to a range.
- PyXLL functions can return [pandas DataFrames](https://www.pyxll.com/docs/userguide/pandas.html)!

## Extra Credit

- Use an async function for fetching the data.
- Format your results nicely using PyXLL's cell formatting feature.
- Use matplotlib or plotly to chart results directly in Excel.

## Resources

- [https://en.wikipedia.org/wiki/List_of_Formula_One_drivers]()
- [https://www.pyxll.com]()
- [https://www.crummy.com/software/BeautifulSoup/bs4/doc/]()