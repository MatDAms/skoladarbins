import random
import math
garums = int(input("garuma m"))
platums = int(input("platums m")) # izmeri paralēskaldnim#
biezums = int(input("biezums m"))
x = ("tilpums",garums * platums * biezums)
print (x)

pirma= (145)
otra = (125)#nosaka kura grupa ir darga vai leta#
if pirma > otra:
    print("tik daudz jamaksa",pirma*garums*platums*biezums)#kura grupa tiks izmantota#
else:
    print("tik daudz jamaksa",otra*x)