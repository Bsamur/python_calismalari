print("""/*/*/*/tek-çift sayı/*/*/*/""")


def tek_çift(i):

    if (i%2==0):

        print(i,"sayısı çift")
    else:
        raise ValueError

liste = [34,2,1,3,33,100,61,1800]

for i in liste:
    try:
        print(tek_çift(i))
    except ValueError:
        pass


