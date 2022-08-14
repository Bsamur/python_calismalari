import numpy as np
import pandas as pd

df1=pd.DataFrame({"çalisan":["bahadır","Ahmet","tan","kemal","niyazi"],
                  "grup":["mühendislik","satis","muhasebe","İK","yazılım"]})

df2=pd.DataFrame({"çalisan":["bahadır","Ahmet","tan","kemal","niyazi"],
                  "isegiris":[2012,2010,2005,2003,2021]})
df3=pd.merge(df1,df2)
print(df3)