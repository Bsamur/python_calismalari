
class Eleman2():
    def __init__(self):#init metodunda verilen ilk paremetre örneği temsil eder.
        self.liste=[]


ornek1=Eleman2()
ornek2=Eleman2()

ornek1.liste.append("tan erkoç")
ornek2.liste.append("tan er koç")

print(ornek1.liste,"\n ",ornek2.liste)
"""
#iki tip property vardır:
1-class attribute
2-ınstance Attribute
iki tip method vardır:
1-class method
2-instance method
"""
class Dene1():

    def yaz():#classın altındaki ve içi boş methodlar class methodu olduğunu gösterir.
        print("hello world")
class Dene2():
    metin=input("metin giriniz")
    if metin=="tan":#classın altına if örneği oluyormu diye yaptık
        print("merhaba tan")
#Dene2()
#class method doğrudan örnek üzerinden ılaşılamaz
ornek1=Dene1()
ornek1.yaz()
