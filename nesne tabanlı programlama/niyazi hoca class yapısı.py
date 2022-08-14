#class yapısı
class Ogrenci():
    ogrenci_liste=[]#class property
    def __init__(self,ad,soyadi):
        self.isim=ad #ornek property
        self.soyisim=soyadi
        self.dersler=[]
        self.ogrenci_ekle()#ogrenci oluşturulduğu zaman ek bir ogrenci ekleyi çağırmaya gerek kalmadan eklemek için
    def ogrenci_ekle(self):
        self.ogrenci_liste.append(self.isim+" "+self.soyisim)
    def ders_ekle(self,ders):
        self.dersler.append(ders)
    def ders_sil(self,ders):
        self.ind=self.dersler.index(ders)
        del self.dersler[self.ind]
        print(self.dersler)
    def ders_listele(self):
        print(self.dersler)

ogrenci1=Ogrenci("ali","turkoglu")

ogrenci1.ders_ekle("C#")
ogrenci1.ders_ekle("java")
ogrenci2=Ogrenci("ahmt","tek")
ogrenci2.ders_ekle("python")
print(ogrenci1.dersler)
print(ogrenci2.dersler)
print(ogrenci2.ogrenci_liste)
ogrenci1.ders_listele()
ogrenci1.ders_sil("C#")


