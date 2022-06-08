# APUG Jun 2022

## opendata.scot
The opendata.scot project has 3 main service areas:
- Listing available datasets
- Providing insights on available datasets
- Providing additional learning resources

The core of the service relies on retrieving metadata from a source, cleaning and processing the metadata to a common standard, adding it to the common store, then processing it for display in the frontend.


Read more about the project in the [project wiki](https://github.com/OpenDataScotland/the_od_bods/wiki/About-the-OD_BODS-project)


## Challenge 1 - Scrape new data source (Advanced)
Create a new scraper to scrape data from the National Library of Scotland

This is an existing ticket: [Add National Library of Scotland as a source #62](https://github.com/OpenDataScotland/the_od_bods/issues/62)

We suggest starting with the organisational data section as it only contains [.csv files](https://data.nls.uk/data/organisational-data/)

Tip: there are existing scrapers which can be used as a base and modified [the_od_bods/web-scrapers/](https://github.com/OpenDataScotland/the_od_bods/tree/main/web-scrapers)


## Challenge 2 - Add new data to common store (Beginner)
Challenge 1 can be skipped by creating a local csv file containing metadata. Conveniently, the National Library of Scotland has already created one called the [National Library of Scotland Open Data Register (CSV)](https://data.nls.uk/about/standards/)

1. Locate and download the register
2. Create a .py or .ipynb file to process the relevant data so that it can be added to the [standard store](https://github.com/OpenDataScotland/the_od_bods/blob/main/data/merged_output.csv)
3. Add the script you have created to the [merge_data.py](https://github.com/OpenDataScotland/the_od_bods/blob/main/merge_data.py) process


## Challenge 3 - Get the number of site visits in last 7 days (Beginner)
In a not too distant future, [@opendata_sco](https://twitter.com/opendata_sco) could auto-tweet the most visited dataset of the week. We could even create a top-of-the-pops charts style competition like "Dataset A has been #1 for 3 consecutive weeks".

*BUT* that would require some more work. For now, what we can get is the total number of site visits in the last 7 days, and maybe even create a simple chart of page trends just like the [Gender Pay Gap twitter bot](https://twitter.com/PayGapApp) does.

The [web analytics data](https://github.com/OpenDataScotland/opendata.scot_analytics/tree/main/timeseries) for opendata.scot comes in .json format.


## Challenge 4 - Set up a github action (Beginner)
1. Create a .py script to do something simple, like returning the current date/time, or maybe combined with challenge 3.
2. Set up a github action to trigger the script on schedule


## Challenge 5 - Get number instances from each data file (Advanced)

This is an existing ticket: [Get number instances from each data file #24 ](https://github.com/OpenDataScotland/the_od_bods/issues/24)

Can we add a new metadata attribute to our standard data store which calls out how many instances of data there are in a dataset? This means we can display this information to a browsing user before they decide if they want to download the data. 

Ideally this should be a function we can apply to all datasets in our standard store, but of course there are limitations based on filetype (e.g. pdf files won't have instances). It may be easiest to start with .csv files but the intention should be to apply the same to as many different filetypes as possible.

Tip: this function already exists in the existing web scrapers which can be used as a base and modified [the_od_bods/web-scrapers/](https://github.com/OpenDataScotland/the_od_bods/tree/main/web-scrapers)



## Enjoyed these challenges?
If you liked these challenges, think about [contributing to opendata.scot](https://github.com/OpenDataScotland/the_od_bods/wiki/Contribute-to-the-project) as we add new challenges/features/bugs every month. 

View our open issues/ ideas on the [project board](https://github.com/OpenDataScotland/the_od_bods/projects/1)

