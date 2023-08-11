counter=0
sum= 0
avrage=0
number = input("enter number: ")

while number!= "done" :
    try :
        number=int(number)
    except:
        print("invalid")
    else :
        counter += 1
        sum += number
        avrage = (sum/counter)
        print(f"""you have {counter}number
              that addition is{sum}
              and avrage is {avrage}""")
        number = input("enter number: ")
                
    
    
    
        


    
    

      