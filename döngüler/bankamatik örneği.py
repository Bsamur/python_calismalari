print("""    ***********
azra bank iyi günler diler
   ***********
   Bu bankamatikte yapabileceğiniz işlemler:
   1. para yatırma
   2. para çekme
   3. güncel bakiye sorgulama
   tüm işlemlerden çıkmak için 9 a basın.
""")
bakiye=2500
while True:
    işlemtürü=int(input("işlem numarası giriniz:"))
    if işlemtürü==9 :
        print("azra iyi günler diler")
        break
    elif işlemtürü==1:
        miktar=int(input("miktar giriniz:"))
        if miktar<5:
            print("en az 5 ve 5 tl nin katları şeklinde para yatırabilirsiniz")
            break
        bakiye=miktar+bakiye
        print("güncel bakiyeniz:",bakiye)
    elif işlemtürü==2:
        çekilen_para=int(input("çekmek istediğiniz tutarı giriniz:"))
        if çekilen_para>bakiye:
             print("çekmek istediğiniz tutar ne yazıkki bakiyenizden fazla!")
             break
        elif çekilen_para-bakiye>=0 :
            print("para çekme işleminiz gerçekleştiriliyor...")

        bakiye=bakiye-çekilen_para
        print("güncel bakiyeniz",bakiye)
    elif işlemtürü==3:
        print("güncel bakiyeniz:",bakiye)

    else:
        break
