#with open("eparaksts-timestamps.csv") as file:
 #   for line in file: 
  #      row = line.rstrip().split(",")
   #     print(f"{row[0]} is in {row[1]}")#
#f.close()

# import csv
 
# # opening the CSV file
# with open('pakalpojumu_statistika_03082021.csv', mode ='r')as file:
#   csvFile = csv.reader(file)
# for lines in csvFile:
#         print(lines)
# file.close()

import csv
import random
c = print(random.randrange(0,50))
f = open('cipara_fails.csv', "w")
for i in range (1000):
    number = random.randint(0,50)
    f.write(f"{number}\n")
    print(number)
f.close()