# teszt={'A':('43',0)}
# for i in range(len(teszt['A'][0])):
# print ('A'*int(teszt['A'][0][1]))
# bemenet=input("Add meg a stringet:")
# bemenet=bemenet.upper()
bemenet='KAAAABBBCCDAAAK '
szotar={}
count=1
elozo=bemenet[0]
# A szótár felépitése: keyként a betű,valueként egy lista: [előfordulások stringként,hányszor lett kiirva az adott betu]
butitott=bemenet[0]
# butított string:Itt megmarad a betűk sorrendje,de minden betű csak egyszer szerepel

for i in range(1,len(bemenet)):
    if elozo==bemenet[i]:
        count+=1
        elozo=bemenet[i]
    else:
        butitott+=bemenet[i]
        elozo=bemenet[i]
        if bemenet[i-1] not in szotar:
            szotar[bemenet[i-1]]=[str(count),0]
        else:
            szotar[bemenet[i-1]][0]+=str(count)
        count=1
print(butitott)

