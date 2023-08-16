max =0
number=input("enter number :")
def find_biggest(number,max):
    if  number > max :
        max=number
        return max
        
 
while number !="drop":
    try:
        number=int(number)
    except:
        print("enter an enteger number :")
        number=input("enter number :")
    else:
        max=find_biggest(number,max)
        number=input("enter number :")
        
print(max)    