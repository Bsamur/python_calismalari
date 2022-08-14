#tel rehberi
# ad soyad tel numr istenecek
#soyad ve tel numarasına göre arama yapacak
# yeni kayıt eklenebilecek
#mevcut tüm kayıtları listeleyecek
tel_listesi=[]
isim=input("kişi ismi giriniz: ")
soyisim=input("sayad giriniz: ")
numara=input("numara giriniz")

def yeni_ekle(isim,soyisim,numara):
    while True:
        isim = input("isim giriniz: ")
        soyisim = input("soyad giriniz: ")
        numara = input("numara giriniz: ")
        if emin_misin():
            tel_listesi+= [[isim, soyisim, numara]]

        if devam():
            continue
        else:
            break

def devam():
    a = input("devam etmek istiyor musun (evet,hayır): ")
    if a=="evet":
        return True
    else:
        False
def emin_misin():
    a = input("emin misin (evet,hayır): ")
    if a.lower().startswith("e") or a.upper().startswith("E"):
        return True
    else:
        False

def sorgula():

    if i in tel_listesi:
        if isim==tel_listesi[i[0]]:
            print(tel_listesi[i])
        else:
            print("aradığınız isimde biri bulunmuyor...")
        if soyisim==tel_listesi[i[1]]:
            print(tel_listesi[i])
        else:
            print("aradığınız isimde biri bulunmuyor...")
def getir():
    print(tel_listesi)








