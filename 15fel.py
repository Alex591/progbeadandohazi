
tuplelista=[]
# tuplelista=[('Anna',21,169),('Anna',21,168),('Anna',20,169),('Joska',22,180),('AAnna',20,175)]
#beolvasás menete
while True:
    nev=input('Adj egy nevet: ')
    if nev=='0':
        break
    eletkor=int(input('Adj egy kort: '))
    magassag=int(input('Adj egy magassagot: '))
    tuplelista.append((nev,eletkor,magassag))
#sortolás menete
# sorted függvény:https://docs.python.org/3/howto/sorting.html
b = sorted(sorted(tuplelista, key = lambda x : x[2]), key = lambda x : x[1], reverse = True)
c=sorted(b,key=lambda x:x[0])
for x in c:
    print (x)


