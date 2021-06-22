"""try:

                    Hata çıkarabilecek kodlar buraya yazılıyor.
                    Eğer hata çıkarsa program uygun olan except bloğuna girecek.
                    Hata oluşursa try bloğunun geri kalanındaki işlemler çalışmayacak.
                except Hata1:
                    Hata1 oluştuğunda burası çalışacak.
                except Hata2:
                    Hata2 oluştuğunda burası çalışacak.

                    //
                    //
                    //
"""

while True:
    try:
        sayi1=int(input("Bölünen sayıyı giriniz:"))
        sayi2=int(input("Böleni giriniz:"))
        print("Sonuç:",sayi1/sayi2)
    # except ValueError:
    #     print("Lütfen bir sayı giriniz!")
    # except ZeroDivisionError:
    #     print("Bir sayı 0'a bölünemez! Lütfen farklı bir değer giriniz!")

    except: # Hata ayrımı yapmaksızın her hatada burası çalışır
        print("Lütfen doğru değer giriniz!")
print("Program buradan devam eder..")
