print(""" **********ŞEKİL HESABI
/////////////""")

a="dörtgen"
b="üçgen"
c=input("bulmak istediğniz geometrik şekli yazınız:")

if c==a :
    birinci_kenar=abs(int(input("brinci kenar ölçüsü:")))
    ikinci_kenar=abs(int(input("ikinci kenar ölçüsü:")))
    üçüncü_kenar=abs(int(input("üçüncü kenar ölçüsü:")))
    dördüncü_kenar=abs(int(input("dördüncü keanr ölçüsü:")))
    if birinci_kenar==ikinci_kenar==üçüncü_kenar==dördüncü_kenar:
        print("bu şekil karedir...")
    else:
        print("bu şekil dörtegndir")
elif c==b:
    birinci_kenar = abs(int(input("brinci kenar ölçüsü:")))
    ikinci_kenar = abs(int(input("ikinci kenar ölçüsü:")))
    üçüncü_kenar = abs(int(input("üçüncü kenar ölçüsü:")))
    if birinci_kenar==ikinci_kenar==üçüncü_kenar:
        print("bu şekil eşkenar üçgendir...")
    elif birinci_kenar!=ikinci_kenar==üçüncü_kenar:
        print("bu şekil ikizkenar üçgen...")
    elif birinci_kenar==ikinci_kenar!=üçüncü_kenar:
        print("bu şekil ikizkenar üçgen...")
elif c!=a==b:
    print("yanlış değer girdiniz...")
