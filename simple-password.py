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
