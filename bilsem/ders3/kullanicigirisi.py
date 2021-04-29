#kullanıcı adı admin parola 123456 olan bir kullanıcı giriş ekranı doğru girildiğinde başarılı giriş yanlış olduğunda şifre ya da kullanıcı adı hatalı

kullaniciadi=input("Kullanıcı adınız?")

if kullaniciadi=="admin":
    sifre=(input("Şifre giriniz?"))

    if sifre==("123456"):
        print ("Başarılı giriş")
    else:
        print("Hatalı giriş")
else:
    print("Hatalı giriş")