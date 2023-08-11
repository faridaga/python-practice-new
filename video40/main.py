
height = float(input("please input height"))
weight =float(input("please input weight"))
         
bmi=round(weight /  height**2,2)

if bmi < 18.5 :
    print(f"youre bmi is {bmi} , youre under weight")
    
elif bmi < 25 :
     print(f"youre bmi is {bmi} ,youre weight normal")
     
elif bmi < 30 : 
     print(f"youre bmi is {bmi} ,youre over weight")
     
else :
    print(f"youre bmi is{bmi}, youre bmi is obse")
    