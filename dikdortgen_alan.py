def dikdortgen_alani_hesapla():
    try:
        a = float(input("Dikdörtgenin kısa kenarını girin (a): "))
        b = float(input("Dikdörtgenin uzun kenarını girin (b): "))
        alan = a * b
        print(f"Dikdörtgenin alanı: {alan}")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

# Fonksiyonu çağır
dikdortgen_alani_hesapla()
 