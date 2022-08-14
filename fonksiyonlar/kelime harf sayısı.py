#for döngüsü
#iterable for=> for<değişken adı> in <iterable>
#integer for=> for<değişken adı> in range<integer>
def bul(kelime):
    kontrol = ""

    for i in kelime:
        if i not in kontrol:
            kontrol+=i
            say = kelime.count(i)
            print(i, "-", say)







bul("anahtar")