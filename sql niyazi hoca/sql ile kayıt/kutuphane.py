from urllib.response import addinfo
import mysql.connector as sql


menu="""

1-Kitap Kayıt
2-Öğrenci Kayıt
3-Çıkış


"""

class kutuphane():
    def __init__(self):
        a=1



    def kitapKayit (self,adi,yazar) :
        self.adi=adi
        self.yazar=yazar
        self.baglan()

        sorgu=f"insert into kitaplar(adi,yazar) values ('{self.adi}','{self.yazar}');"
        self.cur.execute(sorgu)
        self.db.commit()
        print("veriler başarıyla kaydedildi...")

        self.kapat()


    def baglan (self):
        self.db=sql.connect(user="root",host="127.0.0.1",password="",database="kutuphane")
        self.cur=self.db.cursor()


    def kapat (self):
        self.cur.close()
        self.db.close()

    def ogrenci_kayit(self,adi,soyadi,sehir_Id):
        self.isim=adi
        self.soyisim=soyadi
        self.sehirId=int(sehir_Id)
        self.baglan()

        sorgu=f"""insert into ogrenciler(adi,soyadi,sehir_Id)
        values ('{self.isim}','{self.soyisim},'{self.sehirId}');"""

        self.cur.execute(sorgu)
        self.db.commit

        print("Tan Bey, merhaba,Öğrenci başarıyla kayıt edildi...")

        self.kapat()

while True:

    print(menu)

    secim=input("seçiminiz: ")

    if secim=="1":
        ogr1=kutuphane()

        adi=input("Kitabın adı giriniz: ")
        yazar=input("Kitabın yazarının adını giriniz: ")

        ogr1.kitapKayit(adi,yazar)

    elif secim=="2":
        ogr1=kutuphane()

        adi=input("Öğrencinin adını giriniz: ")
        soyadi=input("Öğrencinin soyadını giriniz: ")
        sehir_Id=input("Şehir Id giriniz: ")

        ogr1.ogrenci_kayit(adi,soyadi,sehir_Id)
        
      
    elif secim=="3":
        print("Program sona erdi.")
        break
     

    else:
        print("Hatalı seçim yaptınız,lütfen doğrusunu seçin.")