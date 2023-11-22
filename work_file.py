# import random
# c = print(random.randrange(0,50))
# f = open('cipari.txt', "w")
# for i in range (1000):
#     number = random.randint(0,50)
#     f.write(f"{number}\n")
#     print(number)
# f.close()

import csv
import random
with open('random_numbers.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['random number'])
    for i in range(50):
        random_number= random.randint(0,1000)
        writer.writerow([random_number])
f.close()