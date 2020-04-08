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

