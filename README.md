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

while verification != password:
    print("Put the password here :")
    verification = input("")


#Clear the console once the password is correct
os.system('cls')
```
