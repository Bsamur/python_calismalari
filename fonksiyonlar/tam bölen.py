def tambölenfonk(sayı):
    tam_bölme=[]
    for i in range(2,sayı):
        if sayı%i==0:
            tam_bölme.append(i)
    return tam_bölme


while True:
    print(""" ******TAM BÖLNENLERİ BULMA FONKSİYONU******
    ÇIKMAK İÇİN Q YA BASABİLİRSİNİZ""")
    sayı=input("bir sayı giriniz:")
    if sayı=="q":
        print("iyi günler, programdan çıkılıyor...")
        break
    else:
        sayı=int(sayı)
        print("girdiğiniz sayının tam bölenleri:",tambölenfonk(sayı))
        if tambölenfonk(sayı)==[]:
            print("asal sayıdır")