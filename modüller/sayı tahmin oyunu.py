import time
import random
print("""****************SAYI TAHMİN OYUNU*******************
                    *****************************
                    ÇIKMAK İÇİN Q YA BASIN!.......""")
tahmin_hakkı=7
tahminideğer=random.randint(1,40)
while True:
    sayı=input("tahmin değeriniz")

    if sayı=="q":
        print("yine bekleriz")
        break
    elif int(sayı) > tahminideğer:
        time.sleep(2)
        print("tekrar bir sayı girin.tahmin değerinizi küçültün")
        tahmin_hakkı-=1
    elif int(sayı) < tahminideğer:
        time.sleep(2)
        print("tekrar bir sayı girin.tahmin değerini artırın")
        tahmin_hakkı -= 1
    else:
        print("tebrikler...")
    if tahmin_hakkı==0:
        print("tahmin hakkı bitti...")
        break




