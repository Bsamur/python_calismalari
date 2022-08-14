import sqlite3 as sql
db=sql.connect(r"C:\Users\LENOVO\Desktop\python_kurs\grup0041\bahadir\kütüphane2.db")
cur=db.cursor()
sorgu="SELECT Id,adi,yazar FROM kitaplar;"
cur.execute(sorgu)
sonuc=cur.fetchall()
for i in sonuc:

    print(i)
cur.close()
db.close()