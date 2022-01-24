import getpass
kullaniciAdi = getpass.getuser()

import socket
bilgisayarAdi = socket.gethostname()
bilgisayarIpAdresi = socket.gethostbyname(socket.gethostname())

# from time import gmtime, strftime
# strftime("%Y-%m-%d %H:%M:%S", gmtime())

sunucuyaGonderilecekMesaj = kullaniciAdi+"___"+bilgisayarAdi+"___"+bilgisayarIpAdresi

import socket
istemciSoketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.2.34"
port = 23457
Buffer_Boyutu = 1024
istemciSoketi.connect((host, port))
print ("Gonderilecek veri: ", sunucuyaGonderilecekMesaj)
istemciSoketi.send(sunucuyaGonderilecekMesaj)
print ("Veri sunucuya basarili bir sekilde gonderildi.")
sunucudanGelenMesaj = istemciSoketi.recv(Buffer_Boyutu)
print ("Sunucudan Gelen Mesaj: ", sunucudanGelenMesaj)

print ("Sunucudan onay mesaji da alindigina gore; istemci tarafinda da baglanti koparilabilir")
istemciSoketi.close()
