import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic

class Tan(QMainWindow):
    def __init__(self):
        super().__init__()
        self.baslat()
        self.btnTopla.clicked.connect(self.topla)
        
    def baslat(self):
        uic.loadUi(r"C:\Users\LENOVO\Desktop\kodlama egzersizleri\sql niyazi hoca\ilk pencerem.ui",self)
        self.show()
    
    def topla(self):
        toplam1=int(self.txtsayi1.text())
        
        toplam2=int(self.txtsayi2.text())
        
        toplamlar=toplam1+toplam2
      
        self.txttoplam.setText(str(toplamlar))
        
app=QApplication(sys.argv)
ex=Tan()
sys.exit(app.exec_())