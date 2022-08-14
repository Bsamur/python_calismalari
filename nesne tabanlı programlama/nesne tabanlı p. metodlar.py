class bkmblm_müh():
    def __init__(self,isim,soyisim,branş,maaş,yetenek,tecrübe):
        self.isim=isim
        self.soyisim=soyisim

        self.branş=branş
        self.maaş=maaş
        self.yetenek=yetenek
        self.tecrübe=tecrübe
    def bilgiler(self):
        print("""
        ********************************
        isim={}
        
        soyisim={}
        
        branş={}
        
        maaş={}
        
        yetenek={}
        
        tecrübe={}
        *********************************
        
        """.format(self.isim,self.soyisim,self.branş,self.maaş,self.yetenek,self.tecrübe))
    def yetenekekle(self,yeni_yetenek):
        print("yeni yetenek eklendi")
        self.yetenek.append(yeni_yetenek)
    def maaşzammı(self,zam):
        print("zam yapıldı")
        self.maaş+=zam
    def branş_değişim(self,yeni_branş):
        print("branş değişimi yapıpldı")
        self.branş=yeni_branş
class yönetim(bkmblm_müh):
    def __init__(self,isim,soyisim,branş,maaş,yetenek,tecrübe,yl):
        super().__init__(isim,soyisim,branş,maaş,yetenek,tecrübe)
        print("yönetim sınıfı")
        self.yl=yl

    def bilgiler(self):
        print("yönetici bilgileri")
        print("isim:{}\nsoyisim:{}\nbranş:{}\nmaaş:{}\nyetenek:{}\ntecrübe:{}\nyükseklisans:{}".format(self.isim,self.soyisim,self.branş,self.maaş,self.yetenek,self.tecrübe,self.yl))
yönetici=yönetim("memduh","aslan","mekatronik",5000,"solid",10,"evet")
yönetici.branş_değişim("arge")
yönetici.bilgiler()
print(yönetici)