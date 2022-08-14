import mysql.connector as sql
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QRadioButton
from PyQt5 import uic
import easygui




class otobus(QMainWindow):
    def __init__(self) :
        super().__init__()
        
        self.basla()
        
        
    def basla(self):
        uic.loadUi(r"C:\Users\LENOVO\Desktop\kodlama egzersizleri\sql niyazi hoca\sql ile kayıt\Otobus.ui",self)
        self.show()
        self.rdbtnerkek.toggled.connect(self.yolcukayit)
        self.tabWidget.setCurrentIndex(0)
        self.Otobus.setEnabled(True)
        self.btnkaydet.clicked.connect(self.yolcukayit)
        
       
        
       
        
    def baglan(self):
        self.db=sql.connect(user="root",host="127.0.0.1",password="",database="otobus")
        self.cur=self.db.cursor()
        
        
    def yolcukayit(self):
        
        yolcuadi=self.txtyolcuadi.text()
        yolcusoyadi=self.txtuolcusoyadi.text()
        yolcutc=self.txtyolcutc.txt()
        cinsiyet=QRadioButton.rdbtnerkek.QRadioButton("Erkek")
        
        if cinsiyet.clicked():
            return("1")
        else:
            return("0")
            
        
        sorgu=f"INSERT INTO yolcu (adi,soyadi,tc_no,cinsiyet_Id) VALUES ('{yolcuadi}','{yolcusoyadi}','{yolcutc}','{cinsiyet}');"
        self.baglan()
        self.cur.execute(sorgu)
        self.db.commit()
        self.kes()
        easygui.msgbox("kayıt başarılı",title="Sonuç:")
        
        
    def kes(self):
        self.cur.close()
        self.db.close()
        
app=QApplication(sys.argv)
uyg=otobus()
sys.exit(app.exec_())
        
  
    



