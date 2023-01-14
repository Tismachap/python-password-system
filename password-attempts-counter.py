import os
from colorama import *
init(autoreset=True)

#Save the password in a variable
password = "password"

#Enter the number of attempts allowed here
attempts = 4

#Ask for password
print(Fore.BLACK+Back.WHITE+"Put the password here :")
verification = input("")

#If the password is incorrect, ask again and reduce the number of remaining attempts
while verification != password:
    attempts -=1
    print(Fore.RED+"Incorrect, only "+str(attempts)+" attempts left\n")
    print(Fore.BLACK+Back.WHITE+"Put the password here :")
    verification = input("")
    
    #Close the program when no more attempts remain
    if attempts == 1:
        quit()


#Clear the console once the password is correct
os.system('cls')
