a=float(input("Ayliq gelirinizL: "))
b=float(input("Umumi xerciniz: "))
if a<=0 or b<0:
    print("Ayliq ve xerc menfi ola bilmez")
else:
    if b>a:
        print("Budce kesiri var")
    elif b*0.8>=a:
        print("Xerclere diqqet et")
    elif b*0.5<a and b*0.8>a:
        print("Bwdc' normaldir")
    else:
        print("Yaxsi qenaet edirsiniz")
print("Qalan pulun miqdariL: ",a-b)
print("Qenaet faizi: ",(a-b)/a*100,"%")

    