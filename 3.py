import pandas as pd

food1={'number':[1,2,3,4,5],'name':['corn','banana','chips','sauce','pizza'],'price':[100,200,33,22,144]}
food2={'number':[1,2,3,4,5],'name':['apple','banana','beans','sauce','pizza'],'price':[100,200,33,22,144]}

table1=pd.DataFrame(food1)
table2=pd.DataFrame(food2)

fusion=pd.merge(table1,table2,on='name')
fusion=pd.merge(table1,table2,on='number')

print(fusion)
