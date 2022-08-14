#varsayışan değer
#default value==> en sağdaki parametreden başlar
#eğer default yerine başka bir sayı girersek default devreden çıkar
def topla1(sayi1,sayi2=5):
    print(sayi1+sayi2)
topla1(2)
topla1(3,48)
#global
def fonk1():
    global a
    a="merhaba"
def fonk():
    print(a)
fonk1()
fonk()
#global değişken oldu
#"""args"""
#*args => arguments --> sonsuz sayıda  paramatre almak için kullnılır
def fonk2(*args):
    toplam=0
    for i in args:
        toplam +=i
    return toplam
print(fonk2(7,5,6,8,5))
