# import math
# class Kalkulators: # izveido clasi
#     def __init__(self, skaits, skaitlis): # ieviesa divus objektus
#         self.skaits = skaits
#         self.skaitlis = skaitlis
#     def saskaitīšana(self): # define metodi ar kuru saskiatis
#         return self.skaits + self.skaitlis
#     def atņemšana (self): # define metodi ar kuru atņems
#         return self.skaits - self.skaitlis
#     def reizināšana(self): # define metodi ar kuru sareizinās
#         return self.skaits * self.skaitlis
#     def dalīšana(self):# define metodi ar kuru sadalīss
#         return self.skaits / self.skaitlis # atgriež skaitli lai parādītu kad rada uz ekrāna

# r1 = Kalkulators(25,5) # abu objektu vērtības

# print(r1.saskaitīšana()) # izprinte metodes rezultātus
# print(r1.atņemšana())
# print(r1.reizināšana())
# print(r1.dalīšana())


# 2.uzdevums

class Taisnastūris:
    def __init__(self, garums,platums):
        self.garums = garums
        self.platums = platums
    def Perimetrs(self):
        return (self.garums + self.platums)*2
    def Laukums(self):
        return self.garums * self.platums
    
class Pararelskaldnis(Taisnastūris):
    def __init__(self,garums,platums,augstums):
        self.garums = garums
        self.paltums = platums
        self.augstums = augstums
    def Tilpums(self):
        return self.garums * self.platums * self.augstums

f1 = Taisnastūris(6,2)
f2 = Pararelskaldnis(6,2,3)

print(f1.Perimetrs())
print(f1.Laukums())
print(f2.Tilpums())