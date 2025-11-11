szoveg=""
try:
    with open("scifi_input_v2.txt",encoding="utf-8")as fajl:
        szoveg = fajl.read()

except IOError as hiba:
    print("Nem sikerült a fájlt beolvasni",hiba)
    
# 1. feladat
lista = []
print(szoveg.split("**"))