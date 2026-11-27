#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:05:34 2026

@author: alli
"""

import pandas as pd

# 1 masala

mahsulotlar ={
    'Mahsulot':['Non', 'Sut', 'Tuqum', 'Yog','Shakar'],
    'Narx':[5000, 12000, 18000, 30000, 14000],
    'Soni':[40,25,30,10,0]
    }

df = pd.DataFrame(mahsulotlar, index=[101,102,103,104,105])
# print(df)
# print(df.head(3))
# print(df.shape)


# 2 masala

# Jami ustuni: narx × soni
df['Jami'] = df['Narx'] * df['Soni']

# Mavjud ustuni: soni 0 dan katta bo'lsa True
df['Mavjud'] = df['Soni'] > 0

# print(df)

# Faqat Mahsulot va Jami ustunlari alohida DataFrame
yangi = df[['Mahsulot', 'Jami']].copy()
# print(yangi)

# 3 masala
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data, columns=['C', 'A', 'D'])
# print(df)

# 4 masala
df = pd.DataFrame({'Ism': ['Ali', 'Vali', 'Gulnora', 'Sardor']}, index=[10, 20, 30, 40])
# print(df)

ball = pd.Series([90, 75, 88], index=[10, 30, 50])
df['Ball'] = ball
# print(df)
# print(df['Ball'].dtype)   # float64
# df['Ball'] = [90, 75, 88]

df = pd.DataFrame({'Ism': ['Ali', 'Vali', 'Gulnora']}, index=[1, 2, 3])
df['A'] = pd.Series([10, 20, 30], index=[3, 2, 1])
df['B'] = [10, 20, 30]
# print(df)


# 5 masala

xarorat = {
    'Toshkent': { 2022:15.2, 2023:15.8, 2024:16.1 },
    'Samarqand': { 2022:14.1, 2023:14.6 },
    'Buxoro': {2023:16, 2024:16.5 }
    }

df = pd.DataFrame(xarorat)
# print(df)
df.index.name ='Yil'
# print(df)
# print(df.T)



# # 6 masala

# df = df.rename(columns={'Toshkent':'Tosh'})
# print(df)

# df['Namangan'] = 13.5
# print(df)

# del df['Samarqand']
# print(df)

# df = df.drop(columns='Namangan')
# print(df)

# print(list(df.columns))

# # 7 masala 

# arr = df.values
# print(arr)

# print(type(arr))
# print(arr.shape)
# print(arr.dtype)

# df['Andijon'] = ['Eski shaxar', 'chinor', 'uzumzor']
# print(df)
# print(df.values.dtype)
# print(df.dtypes)



# # 8 masala
 
# mahsulotlar ={
#     'Mahsulot':['Non', 'Sut', 'Tuqum', 'Yog','Shakar'],
#     'Narx':[5000, 12000, 18000, 30000, 14000],
#     'Soni':[40,25,30,10,0]
#     }


# df = pd.DataFrame(mahsulotlar)
# # print(df)

# m1 = df['Narx'] > 10000
# m2 = df['Soni'] < 20
# m3 = df['Narx'] < 10000
# m4 = df['Soni'] == 0


# print(m1 & m2)
# print(df[m1 & m2])
# print(df[m3 | m4])


# 9 masala



data = {
    'Ism': ['Ali', 'Vali', 'Gulnora', 'Sardor', 'Dilnoza'],
    'Yosh': [25, None, 30, None, 28],
    'Maosh': [500, 600, None, 450, 700]
}
df = pd.DataFrame(data)

print(df.isna().sum())
df['Maosh'] = df['Maosh'].fillna(0)

df['Yosh'] = df['Yosh'].fillna(df['Yosh'].mean())
print(df)

toza = df.dropna()
print(toza)































