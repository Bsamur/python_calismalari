class Dene1():

    def yaz(self):#classın altındaki ve içi boş methodlar class methodu olduğunu gösterir.
        print(self)
#class method doğrudan örnek üzerinden ılaşılamaz
#class metodun içine parametre yazarsak örnek metod olur ve bu sayede örneklendirerek çalıştırabiliriz.
#örnek metodu class üzerinden erişilemez sadece örnek üzerinden erişilir.
#ornek1=Dene1()
#ornek1.yaz()
#ornek2=Dene1#burada ornek 2 class a eşit olur. ama örnek metodu ile çağıramayız.
#class üzerinden parametre gönderirsek
Dene1.yaz("merhaba dünya")
class Dene1():
    def __init__(self):
        a=1# initin fonksiyonunun altı boş olamaz

    def yaz(self):#classın altındaki ve içi boş methodlar class methodu olduğunu gösterir.
        print(self)
