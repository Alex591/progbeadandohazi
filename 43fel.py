# A római számok:
# I=1,V=5 X=10, L=50, C=100,D=500,M=1000
def romaibolarab(betu):
    if betu=='I':
        return 1
    elif betu=='V':
        return 5
    elif betu=='X':
        return 10
    elif betu=='L':
        return 50
    elif betu=='C':
        return 100
    elif betu=='D':
        return 500
    elif betu=='M':
        return 1000
    return 0
    #a return 0 azért kell,ha esetleg egy olyan betű kerülne ide aminek nem kéne itt lennie
osszeg=0
romailista=[]
arablista=[]
#A szótárban lesz majd kulcsként a római szám,értékként pedig az arab,hogy ne kelljen megint kiszamolni
#mégse,mert többször is előfordulhat egy ugyanolyan romai szam
while osszeg<1000:
    inputosszeg=0
    romai=input("Adjon egy római számot: ")
    romailista.append(romai)
    for x in romai:
        arab=romaibolarab(x.upper())
        inputosszeg+=arab
    osszeg+=inputosszeg
    arablista.append(inputosszeg)



for i in range(len(romai)+1):
    print(f"{romailista[i]} : {arablista[i]}")


