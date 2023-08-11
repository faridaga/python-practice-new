number1=int(input("enter number"))
number2=int(input("enternumber"))
opration=input("enter from list * / + -")


def calcuator(number1, number2, opration):
    if opration =="+" :
        return(number1+number2)
    if opration == "-":
        return(number1-number2)
    if opration =="/":
        return(number2/number1)
    if opration =="*":
        return(number1*number2)
        
    
print(calcuator(number2,number1,opration))

        
