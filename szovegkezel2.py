import string

#1. feladat
szöv=""

try:
    with open("string_input.txt","r",encoding = 'utf-8')as fajl:
        
        szöv = fajl.read()
        
except IOError as ex:
    print(ex)

print(szöv)

#2. feladat
szamdb = 0
#print(string.digits)

for karakter in szöv:
    if karakter in string.digits:
        szamdb += 1
        
print("A szám karakterek száma: ",szamdb)

#3. feladat
print(string.punctuation)

speclista=[]

for karakter in szöv:
    if karakter in string.punctuation and karakter not in speclista:
        speclista.append(karakter)

print(speclista)

try:
    with open("string_output.txt","w",encoding = 'utf-8')as fajl:
        
        
        for i in range(len(speclista)):
            fajl.write(speclista[i])
            if i < len(speclista)-1:
                fajl.write(", ")
        
except IOError as ex:
    print(ex)
    
#feladat 4.
print(string.hexdigits)

sorok = szöv.split('\n')
szavak = []

for sor in sorok:
    sor_darabok = sor.split(' ')
    for sordarab in sor_darabok:
        szavak.append(sordarab)
        
for szo in szavak:
    if ("A" or '5' or '3' or 'b' or '?') in szo:
        i = 0
        while i < len(szo) and szo[i] in string.hexdigits:
            i += 1
        if i == len(szo):
            print("megvan",szo)  