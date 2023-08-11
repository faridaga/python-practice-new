# def bigest_Number(number1,number2,number3) :
#     if number1 > number2:
#         if number1 > number3 :
#             return(number1)
#         else :
#             return (number2)
#     if number2 >number3 :
#         return(number2)
#     else :
#         return(number3)


number1=int(input("enter number1: "))
number2=int(input("enter number2: "))
number3=int(input("enter number3: "))

def bigest_in_two_number(number1,number2):
    if number1 > number2 :
        return number1
    else :
        return number2
    
def biggest_in_three_with_two(number1,number2,number3):
    result=bigest_in_two_number(number1 ,number2)
    result2=bigest_in_two_number(result,number3)
    return result2

resul=biggest_in_three_with_two(number1,number2,number3)
print(result )


