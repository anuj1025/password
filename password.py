# make a password easly
# password using python
# after few srcond ago password is genrated

import random

char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstwuvzy123456789!@#$%^&*()_+=[]{}\\"

length = int(input("enter a length of password"))

password = ''

for i in range(length):
    password += random.choice(char)

print(password)