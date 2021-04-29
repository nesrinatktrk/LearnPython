#listeler birden fazla veri tipindeki değerleri içinde tutabilir
isim = "efe"
liste = [1, 2, 3, "efe", 4, 5]
bosliste=[]
bosliste2 = list()
print(type(liste))
print(type(isim))
print(type(bosliste)) #bize değişkenin tipini verir

print(liste)

#listenin elemanlarına ulaşmak
print(liste[3]) #0. indeksten başlar
print(liste[0]) #ilk eleman

#liste eleman sayısı bulma
print(len(liste))