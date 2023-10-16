import csv 
csv_f = open("students.csv")
csv_reader =csv.reader(csv_f)
for line in csv_f:
    print(line)