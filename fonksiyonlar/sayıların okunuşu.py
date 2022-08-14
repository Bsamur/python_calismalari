birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]


def sayılarınokunusu(sayı):
    onlarbasamağı=sayı%10
    birlerbasamağı=sayı//10

    return onlar[birlerbasamağı]+" "+birler[onlarbasamağı]
sayı=int(input("sayı:  "))

print("sayınızın okunuşu:",sayılarınokunusu(sayı))