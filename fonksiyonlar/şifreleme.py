def sifrele(kelime):
    liste=[]
    alfabe="abcçdefgğhıijklmnoprsştuüvyz ,"
    for i in kelime:
        ind=alfabe.index(i)
        liste.append(ind)
    return liste


def decoder(liste):
    alfabe="abcçdefgğhıijklmnoprsştuüvyz ,"
    liste2 = []
    for i in liste:
        x = alfabe[i]
        liste2.append(x)
    return liste2
liste=[15, 5, 19, 9, 0, 1, 0, 28, 4, 24, 16, 26, 0, 29, 28, 16, 0, 20, 10, 14, 20, 10, 16]
a=decoder(liste)

print(a)
for j in a:
    print(j,end="")


