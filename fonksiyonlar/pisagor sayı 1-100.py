def pisagorfonk():
    pisagorlistesi =[]
    for i in range(1,250):
        for j in range(1,250):
             c=(i**2+j**2)**0.5
             if c==int(c):
                pisagorlistesi.append((i,j,int(c)))
    return pisagorlistesi
for i in pisagorfonk():
    print(i)