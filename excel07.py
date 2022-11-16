import pandas as pd

df = pd.read_excel('sample2.xlsx')
df.head()
print(df)
df['LinePrice'] = df['Quantity']*df['UnitPrice']
df.head()
print(df)