import csv

student =[{'No':1,'name':'sreyas','role':'developer'},
          {'No':2,'name':'shaibin','role':'student'},
          {'No':3,'name':'shijo','role':'tester'},
          {'No':3,'name':'sreekanth','role':'student'}]
csv_f =open('name.csv','w')
field_name= list(student[0].keys())

csv_w  =csv.DictWriter(csv_f,fieldnames=field_name)
csv_w.writeheader()
csv_w.writerows(student)
csv_f.close()

csv_file=open('Name.csv','r')
csv_reader=csv.reader(csv_file)
for line in csv_file:
    print (line,end="")