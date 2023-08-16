def even_numbers_sum(first_number,second_number):
    sum=0
    for number in range(first_number,second_number+1) :
        if number % 2 ==0:
            sum += number
    return sum


first_number = int(input("insert first number of range :"))
second_number = int(input("insert second number of range :"))
    
print(even_numbers_sum(first_number,second_number),)

    