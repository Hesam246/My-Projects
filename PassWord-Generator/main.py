import random
import string
import os

# Clearing Terminal
os.system('cls')

# Opening File For Saving The Passwords 
file = open('passwords.txt', "w+")

# Making An Tupple From All Asciis.
options = string.digits + string.ascii_uppercase + string.ascii_lowercase + '!@#$%^&*()_-=-+><}{][|`~'

# Making 8 Difrent Random Choise
passw = random.choices(options, k=8)  

# Taking All 8 Choise`s And Conect Them Example: Without: ['!', '^', 'f', '`', '%', '-', '<', 'x'] With: !^f`%-<x
password = ''.join(passw)

# Print And Save The Password In A File
print(password)
file.write(f'{password}\n')