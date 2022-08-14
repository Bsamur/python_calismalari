def asalsayı(sayı):
    if sayı==1:
        print("1 asal bir sayı değildir.")
        return False
    elif sayı==2:
        print("2 asal bir sayıdır")
        return True
    else:
        for i in range(2,sayı):
            if sayı%i==0:
                return False
        return True

while True:
    sayı=input("bir sayı giriniz:")
    if sayı=="q":
        break
    else:
        sayı=int(sayı)
        if asalsayı(sayı):
            print("asal bir sayıdır",sayı)
        else:
            print(sayı,"asal bir sayı değildir")