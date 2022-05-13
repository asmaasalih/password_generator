""" This project to generate a password consists of upper-case letters , lower-case letters, numbers and sympols
30% upper letters 30% lower letters 20% numbers and 20% punctuation
"""

import string
import random


s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)
password = []


password_length = input(" How many numbers do you want your password? ")
while True:
    try:
        password_length = int(password_length)
        if password_length < 6:
            print("password must be 6 digits or more!")
            password_length = input("Please enter 6 or more. ")
        else:
            break
    except:
        print("please enter numbers only!") 
        password_length = input(" Enter number again! ")


random.shuffle(s1) 
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)
              
part1 = round(password_length*30/100)
part2 = round(password_length*20/100) 

for i in range(part1):           
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])
    
random.shuffle(password)
password = "".join(password)
print(password)        