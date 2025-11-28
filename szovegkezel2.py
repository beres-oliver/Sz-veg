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
print(string.digits)

for karakter in szöv:
    if karakter in string.digits:
        szamdb += 1
        
print(szamdb)