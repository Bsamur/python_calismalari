print("""**********
rehber oluşturma
**********
menu
1-kayıt
2-rehber listele
3-sorgulama
4-düzeltme
5-çıkış

""")


def kayit():#kayıt fonksiyonu

    liste=["adi:","soyadi:","numara:"]
    kyt=""
    uzunluk = len(liste)
    for i in range(len(liste)):
        soru=input(liste[i])
        if i!=2:
            kyt+=soru+","
        else: # numara sorduktan sonra alt satıra geçmesi için.
            kyt+=soru+"\n"

    try:

        with open(r"C:\Users\LENOVO\Desktop\kodlama egzersizleri\dosya işlemleri\rehber.txt", "a",encoding="utf-8") as dosya:
            dosya.write(kyt)
    except Exception as hata:
        print("bir hata oluştu",hata)
def sorgula(soyad):
    try:
        with open(r"C:\Users\LENOVO\Desktop\kodlama egzersizleri\dosya işlemleri\rehber.txt", "r",encoding="utf-8") as dosya:
            oku=dosya.readlines()

            for i in oku:
                print(oku)
                ayir=i.split(",")
                if soyad in ayir[1]:
                    print(i)
                else:
                    print("bu isimde birisi yok")
                    break


    except Exception as hata:
        print("bir hata oluştu", hata)

# dosyamızı listeye dökmek için kullanılır.
def listele():
    with open(r"C:\Users\LENOVO\Desktop\kodlama egzersizleri\dosya işlemleri\rehber.txt", "r",encoding="utf-8") as dosya:
        while True:
            oku=dosya.readline() #yada dosya.readlines() yapıp for i in oku: print(oku) da olabilir.
            if oku == "":
                print("dosya sonu...")
                break
            else:
                print(oku)

while True:
    try:

        secim=int(input("çıkış için 5 ebasın.Seçiminiz: "))
    except Exception as hata:
        print("lütfen işlem numrası girniz.", hata)
    if secim==1:
        kayit()
    elif secim==2:
        listele()
    elif secim==3:
        soyad = input("aramak istediğiniz soyadı giriniz")
        sorgula(soyad)

    elif secim==5:
        print("program kapatıldı....")
        break
