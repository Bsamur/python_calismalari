try:
    dosya=open(r"C:\Users\LENOVO\Desktop\python_kurs\grup0041\bahadir\dosya.txt","r")
    sonuc=dosya.readlines()
    print(sonuc)
except Exception as hata :
    print("hata:",hata)
finally:
    dosya.close()
for i in sonuc:
    print(i)