import easygui
import mysql.connector as sql
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import uic

class Group0041(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.basla()
        
    def basla(self):
        uic.loadUi(r"C:\Users\LENOVO\Desktop\kodlama egzersizleri\sql niyazi hoca\sql ile kayıt\grup0041.ui",self)
        self.show()
        self.tabWidget.setCurrentIndex(0)
        self.tab_2.setEnabled(False)
        self.btncikis.setEnabled(False)
        self.btnGiris.clicked.connect(self.btngir)
        self.btncikis.clicked.connect(self.btnExit)
        self.Btnderskayit.clicked.connect(self.derskayit)
        self.btnogrkaydet.clicked.connect(self.ogretmenkayit)
        
    def baglan(self):
        self.db=sql.connect(user="root",host="127.0.0.1",password="",database="kutuphane")
        self.cur=self.db.cursor()
        
    def kes(self):
        self.cur.close()
        self.db.close()
    def btngir(self):
        adi=self.txtKadi.text()#kullanıcı adi textini alıp okumak için
        sifre=self.txtSifre.text()
        self.tabWidget.setCurrentIndex(1)
        
        try:
            self.baglan()
            sorgu="SELECT  k_adi,sifre FROM kulanicilar"
            self.cur.execute(sorgu)
            gelen=self.cur.fetchall()
            
            for i in gelen:
                if (adi==i[0] and sifre==i[1]):
                    self.lblDurum_2.setText("Giriş başarılı....")
                    self.btncikis.setEnabled(False)
                    self.btnGiris.setEnabled(True)
                    self.tab_2.setEnabled(True)
                    self.btncikis.setEnabled(True)
                    ders="SELECT Id,adi FROM dersler ;"
                    self.cur.execute(ders)
                    getir=self.cur.fetchall()
                    for i in getir:
                        self.cmbders.addItem(str(i[0])+"-"+str(i[1]))
                    break
                else:
                    
                    self.btncikis.setEnabled(False)
                    self.btnGiris.setEnabled(True)
                    self.lblDurum_2.setText("hatalı giriş tekrar deneyiniz...")
                    self.tab_2.setEnabled(False)
                    
                    
                    
           
            
        except Exception as hata:
            self.lblDurum_2.setText("veri girişi hatası..."+(str(hata)))
            print(hata)
            
          
    def btnExit(self):
        self.btncikis.setEnabled(False)
        self.btnGiris.setEnabled(True)
        self.tab_2.setEnabled(False)
        self.kes()
    def ogretmenkayit(self):
        try:
            ders=self.cmbders.currentText()  
            bol=ders.split("-")  
            ders=int(bol[0])
            adi=self.txtogradi.text()
            soyadi=self.txtogrsoyadi.text()
            
            sorgu=f"INSERT INTO ogretmen (adi,soyadi,ders_Id) VALUES ('{adi}','{soyadi}','{ders}');"
            self.baglan()
            self.cur.execute(sorgu)
            self.db.commit()
            self.kes()
            easygui.msgbox("kayıt başarılı",title="Sonuç:")
            
        except Exception as hata:
            easygui.msgbox("hata oluştu"+hata,title="Sonuç:")
            self.txtDerskayit.setText("")
            
    
    def derskayit(self):
        try:
            ders=self.txtDerskayit.text()
            self.baglan()
            sorgu=f"INSERT INTO dersler(adi) VALUES ('{ders}');"
            self.cur.execute(sorgu)
            self.db.commit()
            self.kes()
            easygui.msgbox("kayıt başarılı",title="Sonuç:")
            self.txtDerskayit.setText("")
        except Exception as hata:
            easygui.msgbox("hata oluştu"+hata,title="Sonuç:")
            self.txtDerskayit.setText("")
 
        
        
    
app=QApplication(sys.argv)
ogr=Group0041()
sys.exit(app.exec_())