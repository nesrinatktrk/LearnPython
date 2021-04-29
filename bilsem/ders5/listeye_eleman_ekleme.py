liste=[1,2,3,4,5]
print(liste)
liste.append(6) #listenin sonuna eleman ekler
print(liste)
liste[1]=100
print(liste)
liste.pop()#son elemanı siler
liste.pop(2)#2.indeks silindi
print(liste)

#Sort metodu
liste2 = [50,3,7,"*","/","1nesrin","ali"]
liste2.sort() #listeyi küçükten büyüğe doğru sıralar. String ise a'dan z'ye
print(liste2)
liste2.sort(reverse=True) #listeyi büyükten küçüğe sıralar