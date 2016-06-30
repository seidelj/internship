# Thurday Assigment
Gang, I have uploaded a file called timespent.csv into this folder.  Your first task is to download this file and place it into your internship directory.

A little about this data.  It is the ammount of time, in seconds, that a user has spent on any given page of a website that JL's team is using for an experiment.

Your job is to generate some summary statistics for this data.  In particular we need the mean, median, and max and min values.

You can use whatever means available to python.  I'll give you a hint, Numpy can be very useful for generating two of the above stats.

To get you started, I've started the python script you may use, named sumstats.py.  The code provided in this file will import the data from the csv and assign it to a list variable.

Your finished program should print the statistics to the console.  For example "The mean is: x", "The median is: y".

### Hints
* sorted(*iterable*) is a built in function that returns a new sorted list from the items in iterable
* the timeValues variable is an array_like object, it is also an *iterable*
* the last item of a list can be access at index [-1]
