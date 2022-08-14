import os
def klasor_duzenle():
    dosyalar=[]
    kullanici=input("düzenlemek istediğiniz dosya ismni ve yolunu giriniz:")
    uzantılar=[]
    def list_dir():
        for dosya in os.listdir(kullanici):
            if os.path.isdir(os.path.join(kullanici,dosya)): #girilen klasörmü , dosyamı sorgusu
                continue
            if dosya.startswith("."): #dosyamız gizli bir dosya ise klasör oluşturma
                continue
            else:
                dosyalar.append(dosya)
    list_dir()
    for dosya in dosyalar:
        uzantı=dosya.split(".")[-1]
        if uzantı in uzantılar: #eğer dosyamızın uzantısıyla aynı ad ile dosya zaten varsa tekrar oluşturmuyoruz.
            continue
        else:
                uzantılar.append(uzantı)
    for uzantı in uzantılar:# uzantı isimli klasörleri oluşturuyoruz.
        if os.path.isdir(os.path.join(kullanici,uzantı)):
            continue
        else:
            os.mkdir(os.path.join(kullanici,uzantı))
    for dosya in dosyalar:
        uzantı=dosya.split(".")[-1]
        os.rename(os.path.join(kullanici,dosya),os.path.join(kullanici,uzantı,dosya))
if __name__=="__main__":
    klasor_duzenle()



