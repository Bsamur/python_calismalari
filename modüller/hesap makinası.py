import math
import time
print("""
**********************************
HESAP MAKİNESİ
**********************************
1.TOPLAMA
2.ÇIKARMA
3.ÇARPMA
4.BÖLME
5.COSİNUS(The result is between -pi/2 and pi/2.)
6.SİNUS(The result is between -pi/2 and pi/2.)
7.TANJANT(The result is between -pi/2 and pi/2.)
8.KAREKÖK
9.FAKTÖRYEL
0.ÜSSÜNÜ BULMA
01.OBEB(gcd(*integers)
çıkış için C ye basın***

""")
işlem_numarası=int(input("yapacağınız işlemin numarasını giriniz:"))
çıkış="c"

while True:
    toplam = 0
    if işlem_numarası==1:
        sayı1=int(input("1.sayı giriniz:"))
        sayı2=int(input("2.sayı giriniz:"))

        print(sayı1+sayı2)
        break

    elif işlem_numarası==2:
        sayı1 = int(input("1.sayı giriniz:"))
        sayı2 = int(input("2.sayı giriniz:"))

        print(sayı1 - sayı2)
        break
    elif işlem_numarası == 3:
        sayı1 = int(input("1.sayı giriniz:"))
        sayı2 = int(input("2.sayı giriniz:"))

        print(sayı1 * sayı2)
        break
    elif işlem_numarası == 4:
        sayı1 = int(input("1.sayı giriniz:"))
        sayı2 = int(input("2.sayı giriniz:"))

        print(sayı1 / sayı2)
        break
    elif işlem_numarası==5:
        sayı1 = int(input("sayı giriniz:"))
        print("değer",math.cos(sayı1))
        break
    elif işlem_numarası==6:
        sayı1 = int(input("sayı giriniz:"))
        print("değer",math.sin(sayı1))
        break
    elif işlem_numarası==7:
        sayı1 = int(input("sayı giriniz:"))
        print("değer", math.tan(sayı1))
        break
    elif işlem_numarası==8:
        sayı1 = int(input("sayı giriniz:"))

        print("değer", sayı1**0.5)
        break

    elif işlem_numarası==0:
        sayı1 = int(input("1.sayı giriniz:"))
        sayı2 = int(input("2.sayı giriniz:"))

        print("değer",math.pow(sayı1,sayı2))
        break
    elif işlem_numarası==9:
        sayı1 = int(input("1.sayı giriniz:"))
        sayı2 = int(input("2.sayı giriniz:"))
        sayı3 = int(input("3.sayı giriniz:"))

        print("değer",math.gcd(sayı1,sayı2,sayı3))
        break
    elif işlem_numarası!=[0,1,2,3,4,5,6,7,8,9]:
        çıkış==input("c")
        print("kapanıyor...")
        break












