hesap=1000

try:
    while True:
        print("********************\nATM sistemine hoşgeldiniz\n********************")

        print("""
        İşlemler:

        1. Bakiye Sorgulama
        2. Para Yatırma
        3. Para Çekme

        Programdan 'q' tuşu ile çıkabilirsiniz.

        """)
        kullanici=input("Yapmak istediğiniz işlemin başındaki rakamı girin/ örn: Bakiye sorgulama için 1:")
        
        if kullanici=="1":
            print(hesap)

        elif  kullanici=="2":
            yatirilacakmiktar=int(input("Yatırmak istediğiniz miktarı giriniz:"))
            hesap+=yatirilacakmiktar
            print("Bakiyeniz:",hesap)

        if kullanici=="3":
            çekilecekpara=int(input("Çekilecek parayı giriniz"))
            if (hesap-çekilecekpara<0):
                print("Yetersiz bakiye")
            
            else:
                hesap-=çekilecekpara
                print(hesap)

        elif kullanici=="q":
            break
except ValueError:
    print("Lütfen bir sayı giriniz!")