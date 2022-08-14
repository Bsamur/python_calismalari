import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
import sqlite3 as sql

class Ogrenci(QMainWindow):
        def __init__(self):
                super().__init__()
                self.baslat()
                
        def baslat(self):
                uic.loadUi(r"C:\Users\LENOVO\Desktop\kodlama egzersizleri\sql niyazi hoca\veri çekmek için\kütüphanekitapekle.ui",self)
                self.show()
                self.btnekle.clicked.connect(self.kitapekle)
                
        def baglanti(self):
                self.db=sql.connect(r"C:\Users\LENOVO\Desktop\python_kurs\grup0041\bahadir\kutuphane_yeni.db")
                self.cur=self.db.cursor()
        def kapat(self):
                self.cur.close()
                self.db.close()
        def kitapekle(self):
                adi=self.txtadi.text()
                yazar=self.txtyazar.text()
                sorgu=f"INSERT INTO kitaplar(adi,yazar) VALUES ('{adi}','{yazar}');" 
                
                self.baglanti()
                self.cur.execute(sorgu)
                self.db.commit()
                self.kapat()
                
                print("kayıt başarılı....")

app=QApplication(sys.argv)
ogr=Ogrenci()
sys.exit(app.exec_())