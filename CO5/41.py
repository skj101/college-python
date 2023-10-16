import csv
with open('students.csv','r') as csv_f:
    csv_r =csv.DictReader(csv_f)
    print("Name DOB Email")
    print("---------------------------------")
    for line in csv_r:
        print(line['first_name']+" "+line['last_name'],"",line['date_of_birth'],"",line['email'])   