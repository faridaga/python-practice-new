def leap_Year_fnction_solotion(year):
    if year % 4 ==0 or year %100==0 or year % 400==0 :
        print("its leap") 
    else :
          print("it isnt leap")    
    return(year)
year=int(input("enter year :"))
leap_Year_fnction_solotion(year)
    