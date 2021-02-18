import csv

with open("1.csv", 'w', newline='') as data:
    csvW = csv.writer(data, dialect=("excel"))
    csvW.writerow(['1', '2', '3', '4'])
    csvW.writerow(['a', 'b', 'c', 'd', 'f', 'e'])
