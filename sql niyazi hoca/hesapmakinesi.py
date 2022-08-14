import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic

class Hesap(QMainWindow):
    def __init__(self ) :
        super().__init__()
        self.baslat()
        
        self.metin=""
        
    def baslat(self):
        uic.loadUi(r"C:\Users\LENOVO\Desktop\kodlama egzersizleri\sql niyazi hoca\hesapmakinesi.ui",self)
        self.show()
        self.btn1.clicked.connect(self.d1)
        self.btn2.clicked.connect(self.d2)
        self.btn3.clicked.connect(self.d3)
        self.btn4.clicked.connect(self.d4)
        self.btn5.clicked.connect(self.d5)
        self.btn6.clicked.connect(self.d6)
        self.btn7.clicked.connect(self.d7)
        self.btn8.clicked.connect(self.d8)
        self.btn9.clicked.connect(self.d9)
        self.btn0.clicked.connect(self.d0)
        self.btnsagparantez.clicked.connect(self.sag)
        self.btnsolparantez.clicked.connect(self.sol)
        self.btnarti.clicked.connect(self.arti)
        self.btneksi.clicked.connect(self.eksi)
        self.btncarpi.clicked.connect(self.carpi)
        self.btnbolum.clicked.connect(self.bolu)
        self.btnesit.clicked.connect(self.esit)
        self.bclear.clicked.connect(self.sil)
        
        
        
        
    def d1(self):
        self.metin+="1"
        self.txtekran.setText(str(self.metin))
    def d2(self):
        self.metin+="2"
        self.txtekran.setText(str(self.metin))
    def d3(self):
        self.metin+="3"
        self.txtekran.setText(str(self.metin))
    def d4(self):
        self.metin+="4"
        self.txtekran.setText(str(self.metin))
    def d5(self):
        self.metin+="5"
        self.txtekran.setText(str(self.metin))
    def d6(self):
        self.metin+="6"
        self.txtekran.setText(str(self.metin))
    def d7(self):
        self.metin+="7"
        self.txtekran.setText(str(self.metin))
    def d8(self):
        self.metin+="8"
        self.txtekran.setText(str(self.metin))
    def d9(self):
        self.metin+="9"
        self.txtekran.setText(str(self.metin))
    def d0(self):
        self.metin+="0"
        self.txtekran.setText(str(self.metin))
    def sag(self):
        self.metin+=")"
        self.txtekran.setText(str(self.metin))
    def sol(self):
        self.metin+="("
        self.txtekran.setText(str(self.metin))
    
    def arti(self):
        self.metin+="+"
        self.txtekran.setText(str(self.metin))
    def eksi(self):
        self.metin+="-"
        self.txtekran.setText(str(self.metin))
    def carpi(self):
        self.metin+="*"
        self.txtekran.setText(str(self.metin))
    def esit(self):
        sonuc=eval(self.metin)
        self.txtekran.setText(str(sonuc))
    def bolu(self):  
        self.metin+="/"   
        self.txtekran.setText(str(self.metin))
    def sil(self):
        self.metin=""   
        self.txtekran.clear()
        
        

        
        
    
    
app=QApplication(sys.argv)
orn=Hesap()
sys.exit(app.exec_())