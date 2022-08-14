otobus=dict()
liste=[]
liste2=[]

a=0
while a<41:
    yolcu = input("yolcu adı ve soyadı giriniz:")
    a+=1
    liste.append(yolcu)
    for i in range(len(liste)) :

        otobus[i]=liste[i]
        liste2.append(otobus.keys())

    print(otobus)