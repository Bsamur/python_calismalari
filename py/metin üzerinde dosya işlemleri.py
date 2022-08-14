metin="ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
kaç_adet = dict()
for i in metin:

    if (i in kaç_adet):
        kaç_adet[i]+=1
    else:
        kaç_adet[i]=1

for har,sayı in kaç_adet.items():
    print("{} harfi {} adet bulunmaktadır".format(har,sayı))
