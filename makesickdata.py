# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fwXal82IF-dB2FzSRnO6t_BUw_vQ9EC3
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import codecs
#df = pd.read_csv("/content/hokkaido.csv")
#df.head()

with codecs.open('/content/hokkaido.csv', 'r', 'sjis', 'ignore') as f:
    df = pd.read_csv(f)

df2 = df[3::]

df2 = df2.loc[:,'1':'3.14']

df3 = df2.T

df.columns

sick=df.loc[3::,'Unnamed: 5'].T

age = df.loc[:,'1':'3.14']

age = age[0:3]

age = age.T

df4 = pd.concat([age, df3], axis=1)

df5=pd.DataFrame([["","",""]])

df5

df6 = pd.concat([df5.T, sick.T])

pd.concat([df6.T, df4])

