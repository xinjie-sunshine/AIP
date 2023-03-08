import pandas as pd

df = pd.read_excel('AIP.xlsx', header=None,  index_col=0)
print(df.columns.values)
