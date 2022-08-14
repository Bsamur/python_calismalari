def nothesaplma(satır):
    satır=satır[:-1]
    liste=satır.split(",")
    isim= liste[0]
    not1= int(liste[1])
    not2 =int(liste[2])
    not3 =int(liste[3])
    ortlamanot=(not1+not2+not3)/3
    if ortlamanot>=90:
        harf="AA"
    elif ortlamanot>=80:
        harf="BA"
    elif ortlamanot >= 75:
        harf="BB"
    elif ortlamanot >= 70:
        harf="CB"
    elif ortlamanot >= 60:
        harf="CC"
    elif ortlamanot >= 60:
        harf="CD"
    elif ortlamanot >= 50:
        harf="DD"
    else:
        ortlamanot >= 40
        harf="F"
    return isim+","+harf+"\n"

with open("dosya.txt","r",encoding="utf-8") as file:
    sınav_notu_listesi = list()
    for i in file:

        sınav_notu_listesi.append(nothesaplma(i))
    with open("geçen_kalan_listesi.txt","w",encoding="utf-8")as file2:
        for i in sınav_notu_listesi:
            file2.write(i)
with open("geçen_kalan_listesi.txt","r",encoding="utf-8") as file3:
    kalanlar=list()
    geçenler=list()

    for x in file3:
        x=x[:-1]
        öğrenci=x.split(",")
        if öğrenci[1]=="F":
            kalanlar.append(x+"\n")
        elif öğrenci[1]!="F":
            geçenler.append(x+"\n")

    with open("kalanlar.doc","w",encoding="utf-8") as file4:
        for a in kalanlar:
            file4.write(a)
    with open("geçenler.xls","w",encoding="utf-8") as file5:
        for a in geçenler:
            file5.write(a)

















