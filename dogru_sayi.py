int_sayi = 5
while True:
    alinan_sayi = int(input("Bir sayı tahmin edin: "))
    
    if int_sayi == alinan_sayi:
        print("Tebrikler! Doğru tahmin.")
        break
    else:
        print("Yanlış tahmin, tekrar deneyin.")