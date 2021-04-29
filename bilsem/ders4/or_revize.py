"""Bir önceki örnekteki or'lu şartı or kullanmadan yap."""
sayi = int(input("lütfen 0'dan küçük veya 100'den büyük bir sayı giriniz"))
if not 0 < sayi < 100: #0 ile 100 arasında değilse
    print("Sayı tuttu.")
else:
    print("Yönergeyi tekrar oku ve dikkatlice yeni bir sayı gir")