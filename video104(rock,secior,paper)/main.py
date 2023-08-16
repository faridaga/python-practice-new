import random

answer=input("enter rock/sesiro/paper :")
list = ["sesior", "paper", "rock"]

comuters_answer=""
wana_play=input("do you want to play  y/n ?")

while wana_play =="y":
    counter = int(random.randint(0,2))
    comuters_answer = list[counter]

    if answer==comuters_answer:
        print("equal")
        print(f"compter answer is:{comuters_answer}")
        wana_play=input("do you want to play again y/n ?")
        answer=input("enter rock/sesiro/paper :")
        
    if answer=="sesiour" and comuters_answer== "paper"or answer=="rock" and comuters_answer== "paper" or answer=="paper" and comuters_answer== "rock":
        print("you won")
        print(f"compter answer is: {comuters_answer}")
        wana_play=input("do you want to play again y/n ?")
        answer=input("enter rock/sesiro/paper :")
         
    if answer=="paper" and comuters_answer== "sesior" or answer=="sesiour" and comuters_answer== "rock" or answer=="paper" and comuters_answer== "rock":
        print("computer won")
        print(f"compter answer is: {comuters_answer}")
        wana_play=input("do you want to play again y/n ?")
        answer=input("enter rock/sesiro/paper :")
        
    
 
        
    

