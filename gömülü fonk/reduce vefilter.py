liste=[1,2,3,4,5,6,7,8,9,10]
çift=list(filter(lambda x:x%2==0,liste))
from functools import reduce
print(reduce(lambda x,y:x+y,çift))
print(çift)