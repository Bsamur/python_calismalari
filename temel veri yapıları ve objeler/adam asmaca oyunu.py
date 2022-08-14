import  random as rd
araclar=["bisiklet","motorsiklet","otobüs","scooter","otomobil","tren"]
hayvanlar=["öredek","kaz","kedi","hampster","köpek","balık","kaplumbağa"]

kategori=[araclar,hayvanlar]
secim=rd.choice(kategori)
print(secim)
secim2=rd.choice(secim)
print(secim2)
hayvanlar=["öredek","kaz","kedi","hampster","köpek","balık","kaplumbağa"]
secim3=rd.choices(hayvanlar,k=3)#choices kullanımı kaç değer verirsek o kadar rastgele o kadar değer getirir.
print(secim3)