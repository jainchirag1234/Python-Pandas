import pandas as pd

Employee={'number':[1,2,3,4,5],"name":["abby","bac","can","don","eih"],"hourly salary":[11,12,13,14,15]}
table1=pd.DataFrame(Employee)
print(table1.head(1))
print(table1.tail(1))
