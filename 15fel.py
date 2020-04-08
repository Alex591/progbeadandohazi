








tuplelista=[]

#beolvasás menete
while True:
    nev=input('Adj egy nevet: ')
    if nev=='0':
        break
    eletkor=int(input('Adj egy kort: '))
    magassag=int(input('Adj egy magassagot: '))
    tuplelista.append((nev,eletkor,magassag))
#sortolás menete
