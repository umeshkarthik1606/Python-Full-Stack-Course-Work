'''import csv
with open('sample.csv','r') as file:
    content = csv.reader(file)
    for row in content:
        print(row[2])
'''
import csv
with open("sample.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["6","Nitesh","PFS"])
    
