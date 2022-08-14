class Dene1():
    def __init__(self):
        self.isim="tan erkoç"
        self.a=1# init fonksiyonunun altı boş olamaz

    def yaz(self):#classın altındaki ve içi boş methodlar class methodu olduğunu gösterir.
        print(self)
    @classmethod
    def clsmtd(cls):
        print("selam herkese")
    @staticmethod
    def sttcmtd():
        print("@staticmethod methodun diğerinden tek farkı parametre almaz ")


# @classmethod a örnek veya class üzerinden erişilebilir

#class Dene5(Dene1):
    #def __init__(self):
        #super().__init__()#super kalıtımı sağlar isim i kullanabiliriz.
        #b=1
class Dene3(Dene1):
    def __init__(self):#classın kendi initi var sa kalıtım yapmak için altta super kullanmak zorundayız.
        super().__init__()
        self.b=1
ornek1=Dene3()
print(ornek1.isim)