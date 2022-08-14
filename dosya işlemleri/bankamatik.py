#bir kişinin 1,2 hatta 10 hesabı olabilir
#hesaplar arası para tranferi,para çekme , para yatırma
#ek bir dosyada yapılan işlemler yazılacak. ör: para çekme 2.5.2022 14:35 hesaptan para çekme.
from datetime import datetime
simdi=datetime.now()
bugun=simdi.strftime("%d/%m/%Y %H:%M:%S")
print(bugun)
