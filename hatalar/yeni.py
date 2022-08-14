for i in range(5):
 try:
     sayi1=int(input("lütfen 1. sayıyı girin"))
     sayi2=int(input("lütfen 2. sayıyı girin"))
     toplam=sayi1+sayi2
     print(toplam)
 except Exception as hata:
    print("bir hata oluştu",hata)
 finally:
    print("bu satır her durumda çalışır")