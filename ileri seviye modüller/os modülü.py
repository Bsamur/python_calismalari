import os
for klasöryolu,klasöradı,dosyaismi in os.walk("C:/Users/LENOVO/Desktop"):
    for a in dosyaismi:
        if (a.endswith(".SLDPRT")):
            print(a)
while True:


    os.startfile("C:/Users/LENOVO/Desktop/çizim/105 BLANK HOLDER 20 MM ARA PLAKA (BOŞALTMALI).DWG")