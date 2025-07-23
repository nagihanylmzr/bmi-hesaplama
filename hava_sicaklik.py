#C = 5/9(F-32)

def donusum():
    sicaklik_fahrenheit=input("hava sicakligini giriniz(fahrenheit) olarak giriniz.")
    F=float(sicaklik_fahrenheit)
    celcius=5/9 *(F-32)
    print(celcius)

    if celcius> 30:
        print("hava sicak")
    else:
        print("hava soguk")
 
donusum()