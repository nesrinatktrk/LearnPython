import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
# Gmail email sunucusuna bağlanıyoruz
try:
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

    body_text = MIMEText(body, "plain")  
    mesaj.attach(body_text) 
    mail.sendmail( mesaj["From"], mesaj["To"], mesaj.as_string())
    print("Mail başarılı bir şekilde gönderildi.")
    mail.close()
except:
    print("Hata:", sys.exc_info()[0])
