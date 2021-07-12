import random
print("""TAŞ KAĞIT MAKAS OYUNUNA HOŞ GELDİNİZ:
Taş için 1;
Kağıt için 2;
Makas için 3 rakamlarını tuşlayın.
Bilgisayara karşı oynanır
3 olan kazanır. Bol şans...
""")
liste1=[]
liste2=[]
while True:
    try:
        oyuncu1=int(input("1. oyuncu:"))
        bot=random.randint(1,3)
        if oyuncu1==1 and bot==1:
            print("Sen taş yaptın, bilgisayar da taş yaptı.")
            print("berabere, sayı yok :(")
        elif oyuncu1==1 and bot==2:
            liste2.append(1)
            print("Sen taş yaptın, bilgisayar kağıt yaptı.")
            print("Senin puanın.",(len(liste1)))
            print("Bilgisayarın puanı:",(len(liste2)))
        elif oyuncu1==1 and bot==3:
            liste1.append(1)
            print("Sen taş yaptın, bilgisyar makas yaptı.")
            print("Senin puanın:",(len(liste1)))
            print("Bilgisayarın puanı:",(len(liste2)))

        if oyuncu1==2 and bot==1:
            liste1.append(1)
            print("Sen kağıt yaptın, bilgisayar taş yaptı.")
            print("Senin puanın.",(len(liste1)))
            print("Bilgisayarın puanı:",(len(liste2)))
        elif oyuncu1==2 and bot==2:
            print("Sen kağıt yaptın, bilgisayar da kağıt yaptı.")
            print("berabere, sayı yok :(")
        elif oyuncu1==2 and bot==3:
            liste2.append(1)
            print("Sen kağıt yaptın, bilgisyar makas yaptı.")
            print("Senin puanın:",(len(liste1)))
            print("Bilgisayarın puanı:",(len(liste2)))

        if oyuncu1==3 and bot==1:
            liste2.append(1)
            print("Sen makas yaptın, bilgisayar taş yaptı.")
            print("Senin puanın.",(len(liste1)))
            print("Bilgisayarın puanı:",(len(liste2)))
        elif oyuncu1==3 and bot==2:
            liste1.append(1)
            print("Sen makas yaptın, bilgisayar kağıt yaptı.")
            print("Senin puanın.",(len(liste1)))
            print("Bilgisayarın puanı:",(len(liste2)))
        elif oyuncu1==3 and bot==3:
            liste2.append(1)
            print("Sen makas yaptın, bilgisyar da makas yaptı.")
            print("Senin puanın:",(len(liste1)))
            print("Bilgisayarın puanı:",(len(liste2)))

        if len(liste2) == 3:
            print("Kaybettin :(")
            break
        if len(liste1) == 3:
            print("Kazandın :D")
            break

        if oyuncu1 < 1:
            print("Lütfen geçerli bir sayı giriniz!")
        if oyuncu1 > 3:
            print("Lütfen geçerli bir sayı giriniz!")
        
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz!")