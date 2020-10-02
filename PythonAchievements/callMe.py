import sys
import time

def callMe(name1, name2):
    print(name2+" belt naar "+name1)
    time.sleep(1)
    print(name1+": Hallo met "+name1+".")
    time.sleep(1)
    print(name2+": Hey "+name1+" je spreekt met "+name2+", hoe gaat het?")
    time.sleep(1)
    print(name1+": Hey "+name2+", met mij gaat het goed. Ik heb het alleen erg druk. Is het goed als ik je later terugbel?")
    time.sleep(1)
    print(name2+": Ja hoor, is goed. Ik spreek je later.")
    time.sleep(1)
    print(name1+": Later")
    time.sleep(1)
    print("*beep beep beep*")

callMe(sys.argv[1], sys.argv[2])