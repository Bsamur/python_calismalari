liste1=[1,2,3,4,5]
liste2=[6,7,8,9,10,11]
liste3=[12,13,14,15,16]
liste4=list(map(lambda x,y,z:x*y*z,liste3,liste2,liste1))
print(liste4[2])
from functools import reduce
def maksimum(x,y):
    if x>y:
        return x
    else:
        return y

liste5=[reduce(maksimum,liste3)]
print(liste5)

def asalsayı(x):
    i=2
    if x==1:
        return False
    elif x==2:
        return True
    else:
        while x>i:
            if x%i==0:
                return False
            i+=1
        return True

listem=list(filter(asalsayı,range(1,250)))
print(listem)
def alan(x):
    return x[0]*x[1]
liste= [(3,4),(10,3),(5,6),(1,9)]
print(list(map(alan,liste)))

