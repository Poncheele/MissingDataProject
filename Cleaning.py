import pandas as pd

##### First steps 

clients = pd.read_csv("MissingDataProject\Clients.csv", encoding='latin-1', sep=";")
com = pd.read_csv("MissingDataProject\Communications.csv", encoding='latin-1', sep=";")
ventes = pd.read_csv("MissingDataProject\Ventes.csv", encoding='latin-1', sep=";", low_memory=False)

clients = clients.sort_values(by = "CODE CLIENT")
com = com.sort_values(by = "CODE CLIENT")
ventes = ventes.sort_values(by = "CODE_CLIENT")

clients = clients.set_index("CODE CLIENT")
com = com.set_index("CODE CLIENT")
ventes.rename(columns={'CODE_CLIENT': 'CODE CLIENT'}, inplace=True)
ventes = ventes.set_index("CODE CLIENT")

df1 = pd.DataFrame(['a','b','d','e','h'],index = [1,2,4,5,7], columns = ['C1'])
df2 = pd.DataFrame(['AA','BB','CC','EE','FF'],index = [1,2,3,5,6], columns = ['C2'])

client_com = clients.merge(com, how='outer', left_index=True, right_index=True)
df_total = client_com.merge(ventes, how='outer', left_index=True, right_index=True)

df_total.to_csv("MissingDataProject\combined_data.csv")


##### Clean the whole df frame now
import math
df['MAIL'].isna().sum()   #test

df = pd.read_csv("MissingDataProject\combined_data.csv", encoding='latin-1', sep=",")

df2 = pd.DataFrame(df)

for i in range(0,len(df2)) :
    if type(df.iloc[i,2]) is str :
        car = list(df.iloc[i,2])
        if '@' not in list(df.iloc[i,2]) : 
            print(df.iloc[i,2])
        #at_index = car.index('@')
        #df.iloc[i,2] = "".join(car[at_index+1:])

df

df.iloc[9,2]
list(df.iloc[9,2]).index('@')
list(df.iloc[9,2])[6:]
text = "".join(list(df.iloc[9,2])[6:])
df[2,3]
'@' in list(df.iloc[9,2])
for i in df.iloc[1:10,2] :
    print(i)

df2[0:2] = 4

df['MAIL'][0]=4

df.iloc[0,2] = 5