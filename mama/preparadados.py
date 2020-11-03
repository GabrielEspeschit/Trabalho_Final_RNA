import numpy as np
import pandas as pd

df = pd.read_csv('mammographic_masses.data', header=None)

print(df)

#df_fac = df.apply(lambda col: pd.factorize(col, sort=True)[0])
df_fac = df.replace('?', 0)
print(df_fac)
df_fac = df_fac.sample(frac=1)

df_test = df_fac.iloc[int(0.7*len(df)):]
df = df_fac.iloc[:int(0.7*len(df))]


df.to_csv('mammographic_masses_frac.data')
df_test.to_csv('mammographic_masses_frac.test')