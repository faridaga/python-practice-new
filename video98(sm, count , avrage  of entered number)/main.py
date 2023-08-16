total=0
number = 0
number = input("Enter number? ")

def do_sum(number,total):
    total+=number
    return total

while number!= "done":
    try:
        number=int(number)
    except:
        print("enter integer number")
        number = input("Enter number? ")
    else:
        total = do_sum(number,total)
        number = input("Enter number? ")
        
        
print(total)