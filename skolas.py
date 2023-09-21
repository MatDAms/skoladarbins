# aa = [12,13, 14, 15]
# aa.reverse()

# print(len(aa))
# 
# x = int(input("skaitlis"))
# t = 0
# while x != 0:
#     x= x // 10
#     t += 1
# print("resultats", x)
# x= int(input("viens skaitlis"))
# t =int(input("otrasi skaitlis"))
# if x * t <= 1000:
#     print("ir virnads vai mazaks par 1000","skaitlis", x*t)
# else:
#     print( "ir lielaks par 1000", x + t)
# 
import math
def laukums (a,b):
    r = math.pi * a * 2
    t = math.pi * b * 2
    return (r,t)
rev = laukums (56,12)
print(rev)

    



