import random
c = print(random.randrange(0,1000))
f = open('cipari.txt', "w")
for i in range (100):
    number = random.randint(0,1000)
    f.write(f"{number}\n")
    print(number)
f.close()