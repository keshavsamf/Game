
import os



def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')






print("\033[1;32;40m"  + "MADE BY KESHAV SAMF")

verify = input("\033[1;31;40m" + "press enter to continue")

clr()


name = input("\033[1;37;40m" + "enter name (example= Aman):")



print("\033[1;31;40m" + "roses are red")
print("violets are blue")
print("Hey " + name + " ,I love you")

print("\033[1;32;40m" + "next one")

verify = input("\033[1;31;40m" + "press enter to continue")

clr()



print("\033[1;33;40m" + "Roses are red")
print("but I have none for you,")
print(name + " all I can give is my heart to you.")




print("\033[1;32;40m" + "next one")

verify = input("\033[1;31;40m" + "press enter to continue")


clr()


print("\033[1;37;40m" + "Roses are red")
print("and so is the sunset,")
print(name + " I'm really glad that we met.")




