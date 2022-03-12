from ast import Del
import pandas as pd

S1 = pd.read_excel('PARTIEL SIAD 2022.xlsx', sheet_name=0)
#print(data1)
S2 = pd.read_excel('PARTIEL SIAD 2022.xlsx', sheet_name=1)
#print(data2)
S3 = pd.read_excel('PARTIEL SIAD 2022.xlsx', sheet_name=2)

#df = pd.DataFrame([data1, data2, data3])
#pd.DataFrame.head(df)
pd.DataFrame.head(data1)

import statistics as st

# pd.DataFrame.head(data2)

# pd.DataFrame.head(data2['PRODUIT'])
# listA = []
# listA.append(data2['PRODUIT'][23])
# del listA[0]
# listA
# for x in data2['PRODUIT']:
#     if x == 'Produit A':
#         listA.append(x)
# listA

#pd.DataFrame.head(S2)
Tmoy = st.mean(S2['MONTANT'])
Tmoy #Taro du ticket moyen = 93.16468849802183 ~= 93.16 euros

#print(data2.iloc[0])
S1.head()
S1.sort_values('CODE CLIENT')
S1.set_index('CODE CLIENT')
S1.head()
S1['CODE CLIENT'].head()
S1['CSP'].value_counts()
S1['SIT.FAMILIALE'].value_counts()
S1[S1['SIT.FAMILIALE']=='Ouvrier'].first_valid_index()
S1['CSP'][2651]
S2['MONTANT'].value_counts()
S2.head()
print(S1['VILLE'].value_counts())
S1['VILLE'].unique()


S1 = S1.sort_values('CODE CLIENT')
S1 = S1.set_index('CODE CLIENT')
S3 = S3.sort_values('CODE CLIENT')
S3 = S3.set_index('CODE CLIENT')

S4 = pd.merge(S1, S3, left_index=True, right_index=True, how='outer')
del S4['ADRESSE']
