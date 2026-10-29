a=float(input("Tecrube iliniz daxil edin:"))
b=float(input("Texniki musahize balinizi daxil edin(0-100):"))
if a<0 or b>100 or b<0:
    print("Xeta")
else :
    print("Ilkin merheleni kecmisiniz") if a>=2 and b>=70 and b<=100 else "Ilkin merheleni kecmemisiniz"
    if a>=2 and b>=70:
        print("Novbeti merheleye devet olunursunuz")
    elif b>=90:
        print("Guclu namized")
    else: 
        print("Namized uygun deyil")


   
  