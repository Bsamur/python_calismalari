def mükemmelsayıfonk(sayı):
    toplam=0
    for i in range(1,sayı):
        if sayı%i==0:
            toplam+=i
    return toplam==sayı
for i in range(1,1000):
    if mükemmelsayıfonk(i):
        print("mükemmel sayılar",i)


