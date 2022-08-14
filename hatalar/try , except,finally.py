try:
 while True:
     print("""*****KELİME TERS ÇEVİRME****
        """)
     kelime=str(input("kelime girin:"))
     def terscevirme(kelime):
         return kelime[::-1]


     print(terscevirme(kelime))
except ValueError:
    if type(kelime)!=str:
        print("lütfen integer girmeyin.")
