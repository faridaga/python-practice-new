workstime=float(input("hours of work"))
rate=float(input("rate of work"))

if workstime < 40 :
   pay = workstime*rate
   
else :
  hworkstime= workstime-40
  pay= 40*rate+hworkstime*rate*1.5
  
print(f"youre salary is :{pay}")