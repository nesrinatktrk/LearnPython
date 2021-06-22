#listelere çok benzer ama değiştirilemez, sadece okunabilirdir bu yüzden programlarımızda değiştirilmesini istemedğimiz değerleri bir demet içinde depilayabiliriz
demet=("ali","mehmet",3,4,5,"ali") #demet tanımladık
print(demet[1])
print(demet.index("mehmet"))#ali elemanının kaçıncı indeskte olduğunu verir
print(demet.count("ali"))#kaç tane ali elemanı olduğunu bulur