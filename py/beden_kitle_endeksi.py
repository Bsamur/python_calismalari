print("""***********BEDEN KİTLE ENDEKSİ HESAPLAMA
********************
""")
kilo=float(input("kilonuzu giriniz:"))
boy=float(input("boyunuzu giriniz(m)(örnek:1.70 m):"))
beden_kıtle_endeksı=kilo/(boy*boy)
if beden_kıtle_endeksı<=18.5:
    print("BKI={}, zayıf".format(beden_kıtle_endeksı))
elif  25>beden_kıtle_endeksı>18.5:
    print("BKI {}, orta kilo".format(beden_kıtle_endeksı))
elif  30>beden_kıtle_endeksı>=25:
    print("BKI {}, obez".format(beden_kıtle_endeksı))