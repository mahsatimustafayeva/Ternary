a=float(input("Sifarisin meblegi: "))
if a<0:
    print ("Mebleg menfi ola bilmez")
else: 
    print("Endirim qazandiniz") if a >=100 else print("Endirim yoxdur") 
    if a>200:
        print ("Yekun mebleg: ",a*0.8)
    elif a<199.99 and a>=100:
        print ("Yekun mebleg: ",a*0.9)
    else: 
        print("Yekun mebleg: ",a)
