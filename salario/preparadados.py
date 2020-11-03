import numpy as np
import pandas as pd

df = pd.read_csv('adult.data', header=None)
df_test = pd.read_csv('adult.test', header = None)

df_test[[14]] = df_test[[14]].replace(' <=50K.', ' <=50K')
df_test[[14]] = df_test[[14]].replace(' >50K.', ' >50K')


# print(df)
# print(df_test)

df = pd.concat([df, df_test])
df_fac = df.apply(lambda col: pd.factorize(col, sort=True)[0])
df[[1, 3, 5, 6, 7, 8, 9, 13, 14]] = df_fac[[1, 3, 5, 6, 7, 8, 9, 13, 14]]


df_test = df.iloc[32561:]
df = df.iloc[:32561]
# print(df)
# print(df_test)

df.to_csv('adult_fac.data')
df_test.to_csv('adult_fac.test')