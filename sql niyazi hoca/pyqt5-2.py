import sys
from winreg import SetValue
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
class yenibirsey(QMainWindow):
    def __init__(self ) :
        super().__init__()
        self.basla()
        self.btntamam.clicked.connect(self.btn1)
        self.horizontalSlider.valueChanged.connect(self.sldr)
        
    def basla(self):
        uic.loadUi(r"C:\Users\LENOVO\AppData\Roaming\Python\Python310\site-packages\ikincipencerem.ui",self)
        self.show()
    def btn1(self):
        self.metin=self.txtAd.text()       
        
        self.txtMesaj.setText("merhaba "+self.metin)
    def sldr(self):
        self.deger=self.horizontalSlider.value()
        self.progressBar.setValue(self.deger)
app=QApplication(sys.argv)
orn=yenibirsey()
sys.exit(app.exec_())
        