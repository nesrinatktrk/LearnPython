""" kullanıcıdan'lütfen 0'dan küçük veya 100'den büyük bir sayı giriniz.'
şeklinde bir kontrol yapan bir program yapınız"""
sayi = int(input("lütfen 0'dan küçük veya 100'den büyük bir sayı giriniz"))
if sayi < 0 or sayi > 100:
    print("Sayı tuttu.")
else:
    print("Yönergeyi tekrar oku ve dikkatlice yeni bir sayı gir")