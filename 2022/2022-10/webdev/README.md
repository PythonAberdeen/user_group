# APUG October 2022 webdev Challenge

## Get the site running
It is pretty simple once you have docker compose installed, but that step can be a bit of a pain on some platofrms (though generally easier than it was).

https://github.com/emfcamp/Website

## Improve dev data generation
We have some logic to generate dummy data for volunteer system for development https://github.com/emfcamp/Website/blob/main/apps/base/dev/tasks.py#L32

This could do with some improvements. 
- Include some volunteers having signed up for some shifts. 
- Create the shifts based on event dates in the config (https://github.com/emfcamp/Website/blob/main/config/development-example.cfg#L81) so this dummy data doesn't need to be updated manually for every event (and make it much easier to set up dry run events at other times by just changing the event times in the settings). 

## Put back volunteer landing page

During the event this year we got reports of the volunteer landing page showing people shifts with the wrong time. We think some of this could have been that the list of upcoming shifts wasn't sorted initially (there was a fix for that: https://github.com/emfcamp/Website/pull/1223 but could do with confirming that that was actually sorting by time and not alphabetically by string rendering of time or some other broken way) so people were seeing shifts for later days at the top of the list and only noticing the time was wrong and possibly the time rendering in different timezones. Since this was awkward to reproduce I gave up trying to debug it and just removed the page during the event https://github.com/emfcamp/Website/pull/1227

Task is to reinstate this page, but improved so that 
- it is definitely rendering times in the timezone we want (similar to https://github.com/emfcamp/Website/blob/main/models/volunteer/shift.py#L74 possibly with the event_tz used there pulled out to a config variable, or overridable via a config variable, so it is set in one place in case anyone wants to run an event outside the London timezone with this code) 
- split the shifts up by day of the week headings 
- make sure that the shifts are in chronological order under each day
- anything else you can think of to make it clearer

## Volunteer statistics

I would like to have some statistics from the volunteer system.

How many people signed up as volunteers? What proportion of total attendees is that?

How many of the signed up volunteers actually signed up for shifts?

Histogram of how many volunteers did how many shifts.

Some way of showing numbers of shifts that were fully staffed, below max but above min, and below min throughout the festival.

Graph of average time before start of shift that people signed up for it over the event. I think the versions of ShiftEntry will give time that someone signs up but I don't know how to access that so would need to look into sqlalchemy version feature.

Would be nice to have above graphs filterable by role(s). 

What else do you think it might be useful to know about how volunteering went this time to help with planning for next time? 

## Any Other Ticket
https://github.com/emfcamp/Website/issues
