from random import randint,shuffle
symbols=[33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,58,59,60,61,62,63,64,91,92,93,94,95,96,123,124,125,126]
def getupp():
    return chr(randint(65,90))
def getlow():
    return chr(randint(97,122))
def getnum():
    return chr(randint(48,57))
def getsym():
    return chr(symbols[randint(0,31)])
def generate(a):
    password=[getupp(),getlow(),getnum(),getsym()]
    while(len(password)<a):
        match randint(0,3):
            case 0:
                password.append(getupp())
            case 1:
                password.append(getlow())
            case 2:
                password.append(getnum())
            case 3:
                password.append(getsym())
    shuffle(password)
    return "".join(password)
print(generate(int(input("enter the length of the password: "))))
input("Press enter to exit;")