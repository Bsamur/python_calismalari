print("""***********
il plaka uygulaması
***********""")
plaka=int(input("Aradığınız ilin plaka numarasını giriniz: "))

with open(r"C:/Users/LENOVO/Desktop/kodlama egzersizleri/dosya işlemleri/iller.txt","r") as dosya:
    while True:
        oku = dosya.readline()
        sonuc=oku.split(" ")
        if  sonuc[0]==plaka:
            break




