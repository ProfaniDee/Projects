import time
import random
import string

print('Hello, Welcome to the password generator.\n')
length = int(input('How many characters in length would you like your password to be?\n'))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)

password = ''.join(temp)
print('Your custom password is :   ' + password)
