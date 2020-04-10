# teszt={'A':('43',0)}
# for i in range(len(teszt['A'][0])):
# print ('A'*int(teszt['A'][0][1]))
bemenet=input("Add meg a stringet:")
bemenet=bemenet.upper()+' '
# bemenet='AAAABBBCCDAAA '
# A bemenethez hottá lett adva egy space,hogy az utolsó betűk is regisztrálásra kerüljenek
szotar={}
count=1
elozo=bemenet[0]
# A szótár felépitése: keyként a betű,valueként egy lista: [előfordulások stringként,hányszor lett kiirva az adott betu]
butitott=bemenet[0]
# butított string:Itt megmarad a betűk sorrendje,de minden betű csak egyszer szerepel


# Szótár felépitése:
for i in range(1,len(bemenet)):
    if elozo==bemenet[i]:
        count+=1
        elozo=bemenet[i]
    else:
        # megbizonyosodok róla,hogy az általam hozzáadott space ne kerüljön be a butitott stringbe
        if bemenet[i]!=' ':
            butitott+=bemenet[i]
        elozo=bemenet[i]
        if bemenet[i-1] not in szotar:
            szotar[bemenet[i-1]]=[str(count),0]
        else:
            szotar[bemenet[i-1]][0]+=str(count)
        count=1

#Kiirás a butított string segitségével
for x in butitott:
     hanyszor=szotar[x][1]
     print(f"{szotar[x][0][hanyszor]}{x}",end="")
     szotar[x][1]+=1
