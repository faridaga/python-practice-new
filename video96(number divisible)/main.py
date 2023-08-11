list1 = [12, 25 , 30 , 71, 78,88,93,100,200]

def devidile_five(p_list):
    number=0
    for Item in p_list :
         if Item >130 :
             break
         if (Item %5 ==0 ):
            print(Item)
    print("stop")
devidile_five(list1)
            

        
    