import math

def covrage(walls_height,walls_width,covrage_wall):
    area=walls_height*walls_width
    gallonsneed=area/covrage_wall
    cans=math.ceil(gallonsneed)
    print(f"nmber of cans need{cans}")
    
    
walls_height=int(input("enter walls height"))
walls_width=int(input("enter waals wid"))
covrage_wall=int(input("enter corage youre gallons"))


covrage(walls_height,walls_width,covrage_wall)
