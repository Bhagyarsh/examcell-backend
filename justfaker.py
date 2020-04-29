from faker import Faker
import datetime
import csv
fake = Faker()

import csv
data = []
for id in range(0,30):
    classname = fake.name().split()[0]
    startingdate = fake.date_between(start_date='-1y', end_date='+10d')
    endingdate = fake.date_between(start_date=startingdate, end_date='+1y')
    print(id,classname,startingdate,endingdate)
    data.append([id,classname,startingdate,endingdate])
with open("fakedataofkclass.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')

        for line in data:
            print(line)
            writer.writerow(line)


