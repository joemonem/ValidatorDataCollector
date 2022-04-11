import csv

validators = []

with open("validators.csv") as csvfile:
    csvReader = csv.reader(csvfile)
    for row in csvReader:
        validators.append(row[0])

print(validators)
