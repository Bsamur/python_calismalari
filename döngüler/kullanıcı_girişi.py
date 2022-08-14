print("""*******************
giriş sayfası deneme programı
*******************""")

sys_kullanıcı_adı="azra"
sifre="3717"
giris_hakkı=3
while True:
    kullanıcı_adı=input("kullanıcı adı:")
    parola=input("parola:")

    if sys_kullanıcı_adı==kullanıcı_adı and sifre!=parola:
        print("şifre hatalı!...")
        giris_hakkı-=1
    elif sys_kullanıcı_adı!=kullanıcı_adı and sifre==parola:
        print("kullanıcı adı hatalı!...")
        giris_hakkı-=1
    elif sys_kullanıcı_adı!=kullanıcı_adı and sifre!=parola:
        print("kullanıcı adı ve şifre hatalı!...")
        giris_hakkı-=1
    else:
        print("sisteme başarı ile giriş yapıldı")
        break
    if giris_hakkı==0:
        print("giriş hakkınızı doldurdunuz...")
        break
