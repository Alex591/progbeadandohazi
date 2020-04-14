tuplelista = []
# tuplelista=[('Anna',21,169),('Anna',21,168),('Anna',20,169),('Joska',22,180),('AAnna',20,175)]
# beolvasás menete
while True:
    nev = input('Adj egy nevet: ')
    if nev == '0':
        break
    validkore = False
    while not validkore:
        eletkor = input('Adj egy kort: ')
        # hülyeségvédő ha nem egy számot ír be hanem olyasmit,hogy  pl Piroska néni
        if eletkor.isdigit():
            validkore = True
            eletkor = int(eletkor)
    validmagassage = False
    # változó,ami ha a magasság egy számjegy,akkor igaz lesz,másképp kéri folyton az inputot
    while not validmagassage:
        magassag = input('Adj egy magassagot: ')
        if magassag.isdigit():
            validmagassage = True
            magassag = int(magassag)

    tuplelista.append((nev, eletkor, magassag))
# sortolás menete
# sorted függvény:https://docs.python.org/3/howto/sorting.html
# a lambda egy minifüggvény ami visszatér x[1] vagy x[2]-vel,nem érné meg csak ezért függvényt definiálni
b = sorted(sorted(tuplelista, key=lambda x: x[2]), key=lambda x: x[1], reverse=True)
c = sorted(b, key=lambda x: x[0])
for x in c:
    print(x)
