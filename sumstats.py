import csv, os

ROOT = os.path.dirname(os.path.abspath(__file__))

csvFile = os.path.join(ROOT, 'timespent.csv')
with open(csvFile) as f:
    csvReader = csv.reader(f)
    next(csvReader, None)#Skip the first row
    timeValues = []
    for row in csvReader:
        timeValues.append(int(row[0]))

#start your code below

