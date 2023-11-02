def burti_a(fails):
    f= open(fails,'r')
    saturs = f.read()
    skaits = saturs.count('a')
    return skaits
fails="teksts 1.txt"
skaits = burti_a(fails)
print(f"FAilā'{fails}' ir {skaits} burti 'a'")