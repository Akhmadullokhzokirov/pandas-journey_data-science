#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 18:13:08 2026

@author: alli
"""

import pandas as pd

data = {
        'Yil': [2021,2020,2019,2018,2017,2016,2015,2010],
        'Aholi soni':[33.9,33.5,32.9,32.5,31.9,31.4,30.9,28.5],
        'Temp':[1.54,1.48,1.56,1.62,1.65,1.66,1.64,1.53]
        }

df = pd.DataFrame(data)
# print(df.shape)

df = pd.DataFrame(data, columns=['Yil','Temp','Aholi soni','YAIM'], index=['bir',98,97,96,95,94,93,'son'])
# print(df)


aholi = df['Aholi soni']
# print(aholi)

df.YAIM = 0
# print(df)


val = pd.Series([1700,1600,1300], index=['bir',98,97])
df.YAIM=val
print(df)