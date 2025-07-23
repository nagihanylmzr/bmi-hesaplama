def hesa_makinesi(a,b,islem):
    if islem=="+":
        print(a+b)
    elif islem=="-":
         print(a-b)
    elif islem=="*":
        print(a*b)
    elif islem=="/":
        print(a/b)
    else:
        print("gecersiz islem girdiniz")

sayi1=int(input("ilk sayi yi giriniz."))
sayi2=int(input("ikinci sayi yi giriniz."))
_islem=input("yapilacak islemi giriniz. ")
hesa_makinesi(sayi1,sayi2,_islem)