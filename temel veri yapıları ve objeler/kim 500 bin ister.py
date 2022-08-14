#kim 500 bin ister
odul=0
soru1=["türkiyenin çay ili neresidir?",["a-ankara","b-trabzon","c-rize","d-batman"],"c"]
soru2=["hangisi bir yazılım dili değildir",["a-python","b-c++","c-vektör","d-java"],"c"]
soru3=["dünyanın en geniş sınırlara sahip ülkesi",["a-rusya","b-amerika","c-çin","d-bangladeş"],"a"]
soru4=["Türkiyede herkes doğduğu ilde yaşasaydı hangi il en kalabalık olurdu?",["a-ankara","b-şanlıurfa","c-sivas","d-rize"],"b"]
sorular=[soru1,soru2,soru3,soru4]
for i in sorular:
    print(i[0])
    for j in i[1]:
        print(j)

    cevap=input("cevabınız:")
    if cevap==i[2]:
        odul+=1000
        print("tebrikler üst tura hak kazandınız, ödülünüz:",odul)

    else:
        print("elendiniz")
        break