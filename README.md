<div align = center>
  <h1>Password System<h1>
  <img src="https://i.imgur.com/KbHzPrC.png" width="300px" height"300px" href="https://github.com/TismaDll/password-system">
</div>

<p><b>Documentation</b> on how to create a <b>password system</b> using <b>Python</b> in several possible ways and Bonus script</p>
<hr><br>

[**The Easiest Way to Create a Python Password System**](https://github.com/TismaDll/password-system/blob/main/simple-password.py)

```py
import os

#Save the password in a variable
password = "password"

#Ask for password
print("Put the password here :")
verification = input("")

#If the password is incorrect, ask again
while verification != password:
    print("Put the password here :")
    verification = input("")


#Clear the console once the password is correct
os.system('cls')
```
<hr><br>

[**The Easiest Way to Create a Python Password System with Color**](https://github.com/TismaDll/password-system/blob/main/simple-password-color.py)

```py
import os
from colorama import *
init(autoreset=True)

#Save the password in a variable
password = "password

#Ask for password
print(Fore.BLACK+Back.WHITE+"Put the password here :")
verification = input("")

#If the password is incorrect, ask again
while verification != password:
    print(Fore.BLACK+Back.WHITE+"Put the password here :")
    verification = input("")


#Clear the console once the password is correct
os.system('cls')
```
<hr><br>

[**Create a multi-password system with a Array**](https://github.com/TismaDll/password-system/blob/main/array-password.py)

```py
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
```
<hr><br>

[**Add a retry counter**](https://github.com/TismaDll/password-system/blob/main/password-attempts-counter.py)

```py
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

#If the password is incorrect, ask again
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
```
<hr><br>

<h1>Import a Password from Another File</h1>
<p>1- Create a file with a variable and a password</p>
<img src="https://i.imgur.com/576BLUM.png">
<br>

<p>2- Import the file into your main script</p>
<img src="https://i.imgur.com/ea6uzCs.png">
<br>

<p>3- Call the variable</p>
<img src="https://i.imgur.com/tHRKbl0.png">
