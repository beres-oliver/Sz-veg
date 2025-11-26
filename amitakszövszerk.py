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

# 3. feladat
szoveg = szoveg.replace(',','').replace('.','').replace('*','')
print(szoveg)

lista_3 = szoveg.strip().split(' ')
print(lista_3)

try:
    with open("scifi_output.txt",'a',encoding="utf-8")as fajl:
        
        fajl.write("A lista hossza: "+str(len(lista_3))+'\n')

except IOError as hiba:
    print("Nem sikerült a fájlt beolvasni",hiba)

#4. feladat
aslista = []

for elem in lista_3:
    if elem.lower().endswith("és") and elem not in aslista:
        aslista.append(elem)
print(aslista)

try:
    with open("scifi_output.txt","a",encoding = 'utf-8')as fajl:
        
        for elem in aslista:
            fajl.write(elem+"\n")
        
except IOError as ex:
    print(ex)

#5. feladat
alista = []

for elem in lista_3:
    if elem.lower().startswith("a") and (elem.lower() not in ["a","az"]):
        alista.append(elem)
print(len(alista))

#6. feladat
try:
    with open("scifi_output.txt","a",encoding = 'utf-8')as fajl:
        
        fajl.write("A jövőben szó első előfordulásának helye: "+str(szoveg.find("jövőben"))+"\n")
        
except IOError as ex:
    print(ex)

#7. feladat
tizeslista = []

for elem in lista_3:
    elem = elem.lower()
    if len(elem) >= 10 and elem not in tizeslista:
        tizeslista.append(elem)
tizeslista.sort()
print(tizeslista)

try:
    with open("output.txt","w",encoding = 'utf-8')as fajl:
        
        for elem in tizeslista:
            fajl.write(elem+"\n")
        
except IOError as ex:
    print(ex)
