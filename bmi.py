kilo=float(input("Kilonuzu giriniz(kg):"))
boy=float(input("boyunuzu giriniz.(cm):"))
index=boy*boy/kilo

if(boy<0 and kilo<0):
    print("Geçerli bir değer giriniz.")
else:
    index=kilo/(boy*boy)
    print(index)
    if(index>=50):
        print("Fazla kilolusunuz.")
    elif(index>30 and index<50):
        print("Orta kilolusunuz.")
    elif(index<30):
        print("Zayifsiniz.")
kilo = float(input("Kilonuzu giriniz (kg): "))
boy = float(input("Boyunuzu giriniz (cm cinsinde): "))
