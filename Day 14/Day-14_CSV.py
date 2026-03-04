import csv
with open('sample.csv','r') as file:
    data = csv.reader(file)
    for i in data:
        print(i)
