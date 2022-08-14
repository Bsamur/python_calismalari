baş_harfler=""
with open("şiir.txt","r",encoding="utf-8") as file:
    for i in file:
        baş_harfler+=i[0]
    print(baş_harfler)
with open("mail.txt","r",encoding="utf-8") as file2:
    for satır in file2:
        satır=satır[:-1]
        if satır.endswith(".com") and satır.find("@")!=-1:
            print(satır)
isim=["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisim=["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

yeni=list(zip(isim,soyisim))
yeni.sort()
for i,j in yeni:
    print(i,j)