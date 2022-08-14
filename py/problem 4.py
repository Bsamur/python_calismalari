toplam=0
while True:
    sayı=input("bir sayı giriniz:")
    print("çıkmak için q ya basın")
    if sayı=="q":
        break
    sayı=int(sayı)
    toplam += sayı
    print("toplam sayı:{}".format(toplam))
