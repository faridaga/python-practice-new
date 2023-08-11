total=0
def factorial(number):
    if number ==1:
        return 1
    total= number*factorial(number-1)
    return total
    

number=int(input("enter number :"))
print(factorial(number))


