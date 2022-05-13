# Bank
import colorama
from colorama import Fore, Back, Style
import time

colorama.init(autoreset=True)
bal = 1000
bank = input("Please enter a bank name Zain : ")
pass1 = input("Please enter a password Zain : ")
if bank == "Zain" and pass1 == "Zain12":
    print("-------------------------------------------")
    print(Fore.MAGENTA + "Welcome Zain!")
    print("Your balance is", Fore.YELLOW + "$1000")
    print("--------------------------------------------")





else:
    print("----------------------------")
    print(Fore.RED + "Login failed")
    print("----------------------------")
    bank2 = input("Please enter a bank name Eman : ")
    pass2 = input("Please enter a password Eman : ")
    if bank2 == "Eman Qureshi" and pass2 == "ZTINT":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Welcome Eman!")
        print("Your balance is $1000")


    else:
        print("-------------------------")
        print(Fore.RED + "Login failed")
        print("-------------------------")
        bank3 = input("Please enter a bank name Kashaf : ")
        pass3 = input("Please enter a password Kashaf : ")
        if bank3 == "Queen" and pass3 == "109369":
            print("----------------------------------")
            print("Welcome Kashaf!")
            print("Your balance is $1000")

        else:
            print("-------------------------")
            print(Fore.RED + "Login failed")
            print("-------------------------")
            print(Fore.RED + "That's all the accounts we have registered please come back later")
