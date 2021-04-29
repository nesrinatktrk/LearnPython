print("""HESAP MAKİNESİ
1-TOPLAMA
2-ÇIKARMA
3-ÇARPMA
4-BÖLME
Lütfen bir seçim yapınız...
Çıkmak için /"çıkış/" yazınız...""")

islem=input("Seçiminiz:(0,4)")

if islem=="çıkış":
    print("Hoşçakal...")

if islem==:
    sayi1=int(input("1.sayınızı girin:"))
    sayi2=int(input("2.sayınızı girin:"))

    if islem=="1":
        print(sayi1+sayi2)
    elif islem=="2":
        print(sayi1-sayi2)
    elif islem=="3":
        print(sayi1*sayi2)
    elif islem=="4":
        print(sayi1/sayi2)

else islem!="çıkış", "1", "2", "3", "4":
        print("Hatalı seçim!")