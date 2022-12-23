import time
from random import *
import string

#taking input from user
user_pass = input("Enter your password and I will tell you how long it took for me to crack it.  /n")
print('This may take some time, please be patient! May take hours depending on complexity of your password.')
#start timer
start = time.perf_counter()

#storing alphabet letter to use to crack password
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
punctuation = string.punctuation
long_list = lower + upper + numbers + punctuation

# seperate letters and symbols into a dictionary
choices = [*long_list]

#start guessing
guess = ""
while (guess != user_pass):
    guess = ""
    #generate random passwords using for loop
    for letter in range(len(user_pass)):# establishing length of user pass
        guess_letter = choices[randint(0,93)]
        guess = str(guess_letter) + str(guess)

# end timer and figure out total time
end = time.perf_counter()      
total_time = (start - end)  

print(f'Your password is, '+ str(guess) + ' and it took this program ' + str(total_time) + 'seconds to figure it out!')