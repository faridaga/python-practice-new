import random

letters="abcdefghijklmnpqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="123456789"
symbols="!@#$%^&*"

letters_number = int(input("enter lettes number: "))
symbol_numbers = int(input("enter symbol numbers: "))
number_numbers  =int(input("enter number numbers: "))
password_lenght = letters_number+symbol_numbers+number_numbers

password=""

while password_lenght>0:
    type=random.randint(1,3)
    if type==1 and letters_number>0:
        letter_counter=random.randint(0,50)
        password+=letters[letter_counter]
        letters_number -=1
        password_lenght -=1
           
    if type==2 and number_numbers>0: 
        number_counter=random.randint(0,8)
        password +=numbers[number_counter]
        number_numbers -=1
        password_lenght -=1
    if type==3 and symbol_numbers>0:
        symbol_counter=random.randint(0,6)
        password +=symbols[symbol_counter]
        symbol_numbers -=1
        password_lenght -=1
print(password)
    
    
    
        
    
