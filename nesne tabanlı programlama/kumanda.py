import random
import time
class kumanda():
    def __init__(self, tv_durum="Kapalı", tv_ses=0, kanal_listesi=["Trt"], kanal="Trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def tv_açık(self):
        if self.tv_durum=="açık":

            print("tv açıkmış")
        else:

            print("tv açıldı")

            self.tv_durum="açık"
    def tv_kapalı(self):
        if self.tv_durum=="kapalı":

            print("tv kapalı zaten")
        else:
            print("tv kapanıyor")
            self.tv_durum="kapalı"
    def ses_ayar(self):
        while True:
            giriş=input("ses artırma:'>'\nses azaltma:'<'\nçıkış:c\n")
            if giriş==">":
                if self.tv_ses!=20:

                    self.tv_ses+=1
                    print("ses:", self.tv_ses)
            elif giriş=="<":
                if self.tv_ses != 20:

                    self.tv_ses += 1
                    print("ses:",self.tv_ses)
            else:
                print("ses güncellendi")
                break
kumanda1=kumanda()
print("""

Televizyon Uygulaması


1. Tv Aç

2. Tv Kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Sayısını Öğrenme

6. Rastgele Kanala Geçme

7. Televizyon Bilgileri

Çıkmak için 'q' ya basın.
""")
while True:
    işlem=input("yapmak istediğiniz işlem:")
    if işlem =="q":
        print("hoşcakalın...")
        break

    elif işlem=="1":
        kumanda1.tv_açık()

    elif işlem=="2":
        kumanda1.tv_kapalı()

    elif işlem=="3":
        kumanda1.ses_ayar()





