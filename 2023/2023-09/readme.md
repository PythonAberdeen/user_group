# async python

## Challenge 1: wikipedia access stats

Wikipedia used to publish data for access stats to their pages. In 2016 they moved off this to a different system but the old data is still online. 

https://dumps.wikimedia.org/other/pagecounts-all-sites/2016/2016-08/

Grab some of those. Could try downloading them with async python to have multiple files downloading at the same time. Is that any faster than doing it synchronously. 

Find the most accessed page in the period covered by the file dumps you've got. Could run multiple async tasks to process from each file concurrently. Is that any faster?

## Challenge 2: opendata.scot query API

The list of datasets indexed by opendata.scot is available as a big JSON file: https://opendata.scot/datasets.json

Make a REST API server to give a way to query against that and return a subset of the datasets that match the query. 

Can you demonstrate simultaneous requests? Could add sleeps to your processing to simulate it taking more time to make that easier. Try swapping between asyncio.sleep and time.sleep to show the different effect on clients. 

HTTPie could be useful as client for this. https://httpie.io/cli
