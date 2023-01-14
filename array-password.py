import os
from colorama import *
init(autoreset=True)

#Save the password in a variable
password = ["password", "another-password"]

#Ask for password
print(Fore.BLACK+Back.WHITE+"Put the password here :")
verification = input("")

#As long as the entered password is not in the Array "password", ask again
while verification not in password:
    print(Fore.BLACK+Back.WHITE+"Put the password here :")
    verification = input("")


#Clear the console once the password is correct
os.system('cls')
