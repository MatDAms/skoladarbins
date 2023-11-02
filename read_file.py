#f = open("mansteksts.txt", "r")
#print(f.read())#
#f = open("demofile.txt", "r")
#for x in f:
#  print(x)


#f = open("mansteksts.txt", "r")
#print(f.readline())
#f.close()


f = open("mansteksts1.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("mansteksts1.txt", "r")
print(f.read())