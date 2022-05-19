
import os
import json

def check_dir():
    #see if directory exists
    dir_name = input("What is the name of the directory you would like to save to? ")

    if(os.path.exists(dir_name)):
      print("Directory Exists")
    else:
      print("Directory does not exists")

def check_file():
    #create file and contents
    file_name = input("What is the name of the file you would like to save? ")

    with open(file_name, 'w' ) as f:
        names = input("What is your name? ")
        name = names.title()
        address = input("What is your address? ")
        phone = input("What is your phone number? ")
        contents = (name, address, phone)
        json.dump(contents, f)

            #read file back
    with open(file_name,'r') as f:
        print(f.read())
        correct = input('Is this information correct? y/n: ')
        if correct == 'y':
            f.close()
        else:
            check_file()


check_dir()
check_file()


