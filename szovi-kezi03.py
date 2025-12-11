
try:
    with open("input.txt","r",encoding = 'utf-8')as fajl:
        
        karakterlánc = fajl.read()
        
except IOError as ex:
    print(ex)
def feladat1():
    print("Karakterek száma (enterekkel együtt): ",len(karakterlánc))

    karakterláncminuszenter = karakterlánc.replace('\n','')

    print("Karakterek száma (enterek nélkül): ",len(karakterláncminuszenter))
    
    return ("Karakterek száma (enterek nélkül): ",len(karakterláncminuszenter))

def feladat2():
    szavak = karakterlánc.split(' ')

    print("Szavak száma: ",len(szavak))

    return ("Szavak száma: ",len(szavak))

try:
    with open("output.txt","w")as fajl:
        
        fajl.write(f"1. feladat \n {feladat1()}\n")
        
except IOError as ex:
    print(ex)