try:

    class Sistem:

        def calistir(self):

            self.menuGoster()

            secim = self.menuSecimYap()

            print(secim)

            if secim == 1:
                self.Toplama()

            if secim == 2:
                self.Cikarma()

            if secim == 3:
                self.Carpma()

            if secim == 4:
                self.Bolme()

            if secim == 5:
                self.usAlma()

            if secim == 6:
                self.cikis()

            if secim == 7:
                self.yapimciGoster()

        def menuGoster(self):

            print("""        

    ###########################

    # [1] - Toplama           #

    # [2] - Çıkarma           #

    # [3] - Çarpma            #

    # [4] - Bölme             # 

    # [5] - Üssünü Alma       #

    # [6] - Çık               #

    # [7] - Yapımcı           #

    ###########################

            """)

        def menuSecimYap(self):

            while True:

                try:

                    secim = int(input("İşlem Seçiniz : "))

                    while secim < 1 or secim > 7:
                        secim = int(input("Lütfen 1 ila 7 Arasında Değer Giriniz : "))

                    break

                except ValueError:

                    print("[!] Lütfen Sayı Giriniz\n")

            return secim

        def Toplama(self):

            while True:

                try:

                    birinciSayi = int(input("Birinci Sayıyı Giriniz : "))

                    ikinciSayi = int(input("İkinci Sayıyı Giriniz : "))

                    break

                except ValueError:

                    print("[!] Sayı Giriniz")

            toplamSayi = birinciSayi + ikinciSayi

            print(birinciSayi, "+", ikinciSayi, "=", toplamSayi)

        def Cikarma(self):

            while True:

                try:

                    birinciSayi = int(input("Birinci Sayıyı Giriniz : "))

                    ikinciSayi = int(input("İkinci Sayıyı Giriniz : "))

                    break

                except ValueError:

                    print("[!] Sayı Giriniz")

            bulunmusSayi = birinciSayi - ikinciSayi

            print(birinciSayi, "-", ikinciSayi, "=", bulunmusSayi)

        def Carpma(self):

            while True:

                try:

                    birinciSayi = int(input("Birinci Sayıyı Giriniz : "))

                    ikinciSayi = int(input("İkinci Sayıyı Giriniz : "))

                    break

                except ValueError:

                    print("[!] Sayı Giriniz")

            carpilmisSayi = birinciSayi * ikinciSayi

            print(birinciSayi, "x", ikinciSayi, "=", carpilmisSayi)

        def Bolme(self):

            while True:

                try:

                    birinciSayi = int(input("Bölünecek Sayıyı Giriniz : "))

                    ikinciSayi = int(input("Bölecek Sayıyı Giriniz : "))

                    break

                except ValueError:

                    print("[!] Sayı Giriniz")

            bolunmusSayi = birinciSayi / ikinciSayi

            print(birinciSayi, "÷", ikinciSayi, "=", bolunmusSayi)

        def usAlma(self):

            while True:

                try:

                    birinciSayi = int(input("Sayıyı Giriniz : "))

                    ikinciSayi = int(input("Sayının Üssünü Giriniz : "))

                    break

                except ValueError:

                    print("[!] Sayı Giriniz")

            ussuSayi = int(birinciSayi) ** int(ikinciSayi)

            if ikinciSayi == 1:
                print("{birinciSayi}¹".format(birinciSayi=birinciSayi), "=", ussuSayi)

            if ikinciSayi == 2:
                print("{birinciSayi}²".format(birinciSayi=birinciSayi), "=", ussuSayi)

            if ikinciSayi == 3:
                print("{birinciSayi}³".format(birinciSayi=birinciSayi), "=", ussuSayi)

            if ikinciSayi == 4:
                print("{birinciSayi}⁴".format(birinciSayi=birinciSayi), "=", ussuSayi)

            if ikinciSayi == 5:
                print("{birinciSayi}⁵".format(birinciSayi=birinciSayi), "=", ussuSayi)

            if ikinciSayi == 6:
                print("{birinciSayi}⁶".format(birinciSayi=birinciSayi), "=", ussuSayi)

            if ikinciSayi == 7:
                print("{birinciSayi}⁷".format(birinciSayi=birinciSayi), "=", ussuSayi)

            if ikinciSayi == 8:
                print("{birinciSayi}⁸".format(birinciSayi=birinciSayi), "=", ussuSayi)

            if ikinciSayi == 9:
                print("{birinciSayi}⁹".format(birinciSayi=birinciSayi), "=", ussuSayi)

            if ikinciSayi == 0:
                print("{birinciSayi}⁰".format(birinciSayi=birinciSayi), "=", ussuSayi)

        def cikis(self):

            print("Güle Güle")

            quit()

        def yapimciGoster(self):

            print("Yapımcı(Owner) = Bozkurtlig")


    sistem = Sistem()

    while sistem:
        sistem.calistir()

except KeyboardInterrupt:

    print("\nGüle Güle")

    quit()