# APUG March 2022 - Intermediate Challenge

## Introduction

At a previous [Code the City hack weekend](https://codethecity.org/2020/05/25/aberdeen-built-ships/), we scraped (with permission) information on Aberdeen Built Ships from the website and uploaded it to Wikidata. 

Currently on Wikidata 3,064 ships have and Aberdeen Built Ships ID (P8260). 

Curently few (< 1%) of the ships there have a statement for Manufacturer (P176). 

This file on Github shows the number of ships per yard in Github: [https://github.com/CodeTheCity/aberdeen-built-ships/blob/master/ship_builders_qids.csv](https://github.com/CodeTheCity/aberdeen-built-ships/blob/master/ship_builders_qids.csv)

This json file contains the full scraped data: [https://raw.githubusercontent.com/CodeTheCity/aberdeen-built-ships/master/ships.json](https://raw.githubusercontent.com/CodeTheCity/aberdeen-built-ships/master/ships.json)

## The Challenge

1. To create and run query to to show all ships which have an Aberdeen Built Ships ID (P8260) on WIkidata. 

2. To eliminate those ships for which a manufacturer (P176) statement already exists. 

3. Create a plain text file which can be used in Quickstatements - see [Quickstatements help](https://www.wikidata.org/wiki/Help:QuickStatements) to bulk upload statements in the format: 

ship -> Manufacturer -> Yard 

one line per ship. 

Even better to add refererences and date retrieved too. 

This can then be used by an authenticated Wikidata user to upload via Quickstatements to update Wikidata ship items. 

