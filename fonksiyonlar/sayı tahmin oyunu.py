import random as rd
def sayitut():
    sayi=rd.randint(1,100)
    return sayi
sayi=sayitut()
def tahmin(deger):
    if deger>sayi:
        return "aşağı"
    elif deger<sayi:
        return "yukarı"
    else:
        return ("tebrikler doğru bildiniz tutulan değer",sayi)
for i in range(10):
    a=int(input("1-100 arası bir sayı giriniz: "))
    b=tahmin(a)
    print(b)
    if b!="yukarı" and b!="aşağı":
        break

