def faktöriyel(sayı):
    faktöriyel=1
    if sayı==1 or sayı==0:
        print("faktöriyel=",faktöriyel)
    else:
        while sayı>1 or sayı<1:
         sayı=abs(sayı)
         faktöriyel*=sayı
         sayı-=1
    print("faktöriyel=",faktöriyel)





def çarpma_işlemi(*a):
    çarpım=1
    for i in a:
        çarpım *= i
    print("sonuç",çarpım)

çarpma_işlemi(10,20,30)
toplama_işlemi= lambda x,y,z: x+y+z
print(toplama_işlemi(10,20,30))