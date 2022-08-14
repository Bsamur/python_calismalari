#HATA AYIKLAMA
#3 TİP HATA VARDIR
#1. SYNTAX HATASI(YAZIM , İMLA HATASI)
#MANTIKSAL HATALAR,"PROGRAM BUNU AYIKLAYAMAZ"
#RUNTİME HATALARI-ÇALIŞMA ZAMANI HATALARI
#try: hata olabilecek durumda olan kodlar
#except: hata olursa işlenecek kodlar:
#finally
import random


a = 10

sayı = random.randint(1, 100)
while a >= 0:
        try:
            tahmin = int(input("tahmin ettiğniz sayıyı giriniz"))
        except ValueError:
            print("lütfen sayı girin")

            a -= 1
            if a == 0:
                print("tahmin hakkı bitti")

                break
            elif tahmin > sayı:
                print("aşağı ")
                print("kalan tahmin hakkı:", a)
            elif tahmin < sayı:
                print("yukarı")
                print("kalan tahmin hakkı:", a)

            elif tahmin == sayı:
                print("doğru bildiniz")
                print("kalan tahmin hakkı:", a)
                break

