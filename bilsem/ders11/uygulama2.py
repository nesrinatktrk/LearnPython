#hangisinin alanını hesaplamak istiyorsun üçgen kare dikdörtgen ona göre değeer iste fonksiyonla hesapla
while True:
    print("""Alan Hesaplama
    1.Kare
    2.Üçgen
    3.Dikdörtgen
    Çıkış için q'ya basın""")

    kullanici=input("Seçiminiz:")

    def kare(a):
        return a*a
    def üçgen(a,b):
        return a*b/2
    def dikdörtgen(a,b):
        return a*b

    if kullanici == "1":    
        karekenar=int(input("Karenizin bir kenarının uzunluğunu girin:"))
        print(kare(karekenar))

    elif kullanici == "2":
        üçgentaban=int(input("Üçgeninizin taban uzunluğunu girin:"))
        üçgenyükseklik=int(input("Üçgeninizin yüksekliğinin uzunluğunu girin:"))
        print(üçgen(üçgentaban,üçgenyükseklik))

    elif kullanici == "3":
        dikdörtgenkisa=int(input("Dikdörtgeninizin kısa kenarının uzunluğunu girin:"))
        dikdörtgenuzun=int(input("Dikdörtgeninizin uzun kenarının uzunluğunu girin:"))
        print(dikdörtgen(dikdörtgenkisa,dikdörtgenuzun))

    elif kullanici == "q":
        break

    else:
        print("Lütfen geçerli bir seçim yapın")