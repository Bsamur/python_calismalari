menu = """
azra turuizm a.ş
1- kayıt listeleme
2-boş koltukar
3-yolcu listesi
4-yeni kayıt
5-kayıt silme
6-çıkış
"""
koltuk = dict()


def koltuk_tanimla():
    for i in range(1, 41):
        koltuk[i] = "boş"
    return koltuk


koltuklar = koltuk_tanimla()
def liste(sozluk):
    for i, j in sozluk.items():
        print(i, j)


def bos_koltuklar(sozluk):
    bos = 0

    for i, j in sozluk.items():
        if j == "boş":
            bos += 1
            print(i, j)
    if bos > 0:
        print("boş koltuk sayısı", bos)
    else:
        print("Hiç boş koltuk yok")


def dolu_koltuklar(sozluk):
    dolu = 0

    for i, j in sozluk.items():
        if j != "boş":
            dolu += 1
            print(i, j)
    if dolu > 0:
        print("dolu koltuk sayısı", dolu)
    else:
        print("dolu koltuk yok")





def kayit(koltuk_no, isim):
    if koltuklar[koltuk_no] == "boş":
        koltuklar[koltuk_no] = isim
        liste(koltuklar)
    else:
        print("koltuk boş değil...")


def sil(koltuk_no):
    if koltuklar[koltuk_no] != "boş":

        koltuklar[koltuk_no] = "boş"
    else:
        print("koltuk zaten boş")



while True:
    print(menu)
    secim = int(input("liütfen işlem nurası giriniz: "))
    if secim == 1:
        liste(koltuklar)
    elif secim == 2:
        bos_koltuklar(koltuklar)
    elif secim == 3:
        dolu_koltuklar(koltuklar)
    elif secim == 4:
        bos_koltuklar(koltuklar,)
        k_no = int(input("koltuk numarası giriniz: "))
        isim = input("yolcu adı soyadını giriniz: ")
        kayit(k_no, isim)
    elif secim == 5:
        dolu_koltuklar(koltuklar)
        k_no = int(input("silmek istediğiniz koltuk no giriniz: "))
        sil(k_no)
    elif secim==6:
        print("program sona erdi")
        break
    else:
        print("hatalı seçim yaptınız")