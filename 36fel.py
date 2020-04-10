# teszt={'A':('43',0)}
# for i in range(len(teszt['A'][0])):
# print ('A'*int(teszt['A'][0][1]))
# bemenet=input("Add meg a stringet:")
# bemenet=bemenet.upper()
bemenet='AAAABBBCCDAAA'
szotar={}
count=0
elozo=''
for i in range(len(bemenet)):
    if elozo==bemenet[i]:
        count+=1
    else:
        if bemenet[i-1] not in szotar:
            szotar[bemenet[i-1]]=
