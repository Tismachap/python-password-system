<div align = center>
  <h1>Password System<h1>
  <img src="https://i.imgur.com/KbHzPrC.png" width="300px" height"300px" href="https://github.com/TismaDll/password-system">
</div>

<p>Different ways to create password systems with Python</p>
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

[**Create a multi-password system**](https://github.com/TismaDll/password-system/blob/main/array-password.py)

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
