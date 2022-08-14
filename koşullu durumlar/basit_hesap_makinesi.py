print(""" ***********************
basit hesap makinesi
************************
1. işlem=+(1'e basınız)
2. işlem=-(2 ye basınız)
3. işlem=*(3e basınız)
4. işlem=/(4 e basınız)
""")
işlem=int(input("işlem numarası:"))
a=int(input("birinci sayı:"))
b=int(input("ikinci sayı:"))
if işlem==1 :
    print("toplama işlemi sonucu:{}+{}={}".format(a,b,a+b))
elif işlem==2:
    print("çıkarma işlemi sonucu:{}-{}={}".format(a,b,a-b))
elif işlem==3:
   print("çarpma işlemi sonucu:{}*{}={}".format(a,b,a*b))
elif işlem==4:
   print("bölme işlemi sonucu:{}/{}={}".format(a,b,a/b))
else:
    print("yanlış sayı girdiniz")