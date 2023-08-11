def grosspy(hour, rate,gift):
    if hour>40:
       high_hour= hour-40
       pay=40*rate+round(high_hour*rate*gift,2)
    else :
        pay=round(hour*rate,2)
       
    return(pay)

hour=int(input("enter woks hour"))
rate=float(input("input rate for work"))
gift=float(input("gift for over hover work"))
       
pay=grosspy(hour,rate,gift)
print(f"pay {pay}")


    