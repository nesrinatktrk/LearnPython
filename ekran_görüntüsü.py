import os
import pyautogui
import time

ekran_goruntusu = pyautogui.screenshot()  # pyautogui ile ekran görüntüsünü al
dosya_adi = str(time.time_ns()) + ".jpg" #Şu anki zamanı kullanıyoruz böylece isim hiçbir zaman aynı olmuyor

dosya_yolu = os.path.join(r"C:\\Users\Nesrin\Desktop", dosya_adi) # ekran görüntüsünün kaydedileceği yol

ekran_goruntusu.save(dosya_yolu) # ekran görüntüsünü save() fonksiyonu ile kaydediyoruz