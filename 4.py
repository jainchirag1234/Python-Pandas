import pandas as pd

food1={'numbers':[1,2,3,4,5],'name':['apple','banana','chips','popcorn','pizza'],'price':[22,33,44,55,22]}
food2={'colors':["red","yellow","orange","white","blue"],'weight':[120,100,220,210,200],'qt':[1,2,3,4,5]}

table1=pd.DataFrame(food1)
table2=pd.DataFrame(food2)

fusion=table1.join(table2)
print(fusion)
       

