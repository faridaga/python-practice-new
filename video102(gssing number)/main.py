import random
import math

lower =int(input("enter lower bound: "))
upper =int(input("enter upper bound: "))
chanced_number=int(math.log(upper-lower+1,2))
number_genrater = random.randint(lower,upper) 

print(f"\n \tyou have {chanced_number} chance to find number\n \t")
count=0
while  chanced_number > count:
    count +=1
    guess_number=int(input("guess a number: "))
    if guess_number==number_genrater :
        print("congradlation you find the number in {count} try")
        break
    elif guess_number+4>=number_genrater and guess_number-4<= number_genrater :
        print("youre sofar")
    elif guess_number+1>=number_genrater  and number_genrater>  guess_number-1:
        print("youre so near")
    else:
        print("you are so so far")
print(f"the number is :{number_genrater}")