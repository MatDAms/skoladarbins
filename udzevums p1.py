import random
x = str(input("uzrakstiet vardu un uzvardu"))
c =int(input("cik stradajat mēnesi"))#pasaka pamat informaciju#
def darbs(stundas):
    return c*stundas
print(darbs(random.randrange(4)))
if c<40:
    print("ši ir mēneša maksa",darbs)
else:
    print("pieskaita 30 bonosu",darbs)