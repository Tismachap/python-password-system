import os
from colorama import *
init(autoreset=True)

#Save the password in a variable
password = "password"

#Ask for password
print(Fore.BLACK+Back.WHITE+"Put the password here :")
verification = input("")

while verification != password:
    print(Fore.BLACK+Back.WHITE+"Put the password here :")
    verification = input("")

#Clear the console once the password is correct
os.system('cls')
