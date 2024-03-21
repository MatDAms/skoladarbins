import datetime
# class Persona:
#     def __init__(self, name, countr, birth):
#         self.name = name
#         self.countr = countr
#         self.birth = birth
#     def introduce(self):
#         x = datetime.datetime.now()
#         return int((x.strftime('%Y'))) - int(self.birth(0))


# f2 = Persona('alex', 'Japan',(1951,2,2))

# print(f2.introduce())
class Transports:
    def __init__(self, marka, atrums, nobraukums, gads):
        self.mark = marka
        self.atrum = atrums
        self.braukt = nobraukums
        self.gads = gads
    def vec(self):
      return int((datetime.datetime.now().strftime("%Y"))) - int(self.gads(0))
class Autobus(Transports):
    pass



f1 = Transports('volvo','atrums 98', 2000,(1988,6,5))
print(f1.__init__())