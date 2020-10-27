import os

clear = lambda: os.system("cls")

user = input("Username: ")

while True:
    exe = input("etc/cmd/user/-#%s-/Xshell/X~ " % user)

    if exe == 'help':
        print(" ")
        print("help -helps you with commands")
        print("clr -clears screen")
        print("user -show username")
        print("echo -repeats input")
        print("Xshell version -version")
        print("copyright -copyright")
        print(" ")
    elif exe == 'clr':
        clear()
    elif exe == 'user':
        print(" ")
        print(user)
        print(" ")
    elif exe == 'echo':
        eho = input("echo: ")
        print(eho)
    elif exe == 'Xshell version':
        print(" ")
        print("0.1.0")
        print(" ")
    elif exe == 'copyright':
        print(" ")
        print("Silicon Tech")
        print(" ")
        print("Xshell")
        print(" ")
    elif exe == 'ipconf':
        print(" ")
        print("192.168.***.**")
        print(" ")

    else:
        print("!")
        print("syntax error: '%s' is an inoperable command or isn't a command in system" % exe)





