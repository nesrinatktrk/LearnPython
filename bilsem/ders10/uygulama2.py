#fonksiyon 2 tane parametre alacak. Buraya iki sayı gönderilecek. Girilen sayılardan hangisi büyükse o sayı yazılacak.
def buyuksayi(a,c):
    if a<c:
        print("girilen sayılardan büyük olan:", c)
    elif c<a:
        print("girilen sayılardan büyük olan:", a)
    else:
        print("değerler eşit")

sayi1=int(input("Sayı girin"))
sayi2=int(input("2.sayıyı girin"))
buyuksayi(sayi1,sayi2)
