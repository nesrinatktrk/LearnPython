try:
    file=open("bilgiler.txt","r",encoding="utf-8")

except FileNotFoundError:
    print("Dosyayı bulamadım")
finally: # her durumda burası çalışır
    file.close()
