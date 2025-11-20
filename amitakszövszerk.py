szoveg=""
try:
    with open("scifi_input_v2.txt",encoding="utf-8")as fajl:
        szoveg = fajl.read()

except IOError as hiba:
    print("Nem sikerült a fájlt beolvasni",hiba)
    
# 1. feladat
lista = szoveg.split("**")

#print(lista)

for elem in lista:
    elem = elem.strip()
    
#print(lista)

for i in lista:
    if len(i) == 0:
        lista.remove(i)

#print(lista)

# 2. feladat
""" szoveg_kis=szoveg.lower()
print(szoveg_kis) """
for i in range(len(lista)):
     lista[i]=lista[i].lower()
     print(lista[i])
     
print(lista)

for i in range(0,len(lista),2):
    szavak_listája = (lista[i].split(' '))
    szavak_listája[0] = szavak_listája[0].upper()
    lista[i] = ''
    
    for szó in szavak_listája:
        lista[i] += szó + ' '
    
    lista[i] = lista[i].strip()
    
print(lista)

try:
    with open("scifi_output.txt",'w',encoding="utf-8")as fajl:
        
        for sor in lista:
            fajl.write(sor + '\n')

except IOError as hiba:
    print("Nem sikerült a fájlt beolvasni",hiba)
    