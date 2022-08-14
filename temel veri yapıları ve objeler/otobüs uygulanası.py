otobus = dict()
while True:

    for i in range(1, 41):
        otobus[i] = "boş"  # önce otobüs oluştu.
    print(otobus)
    # boş koltuklar
    for i, j in otobus.items():
        if otobus[i] == "boş":
            print(i, j)
    # dolu koltuklar
    for i, j in otobus.items():
        if otobus[i] != "boş":
            print(i, j)

    yolcu = int(input("yolcu koltuk no giirniz:"))
    ad = input("yolcu ad soyad")
    otobus[yolcu] = ad
    print(otobus)
    devam = input("devam edecekmisiniz e/h")
    if devam == "h":
        print("program sona erdi.")
        break