#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 09:35:00 2026

@author: alli
"""

import pandas as pd
from pandas import Series


# 1 masala

shaxarlar  = {
    'Toshkent': 2800, 'Samarqand': 550, 'Buxoro': 280
    }

shaxarlar1 = Series(shaxarlar)
# print(shaxarlar1)
# print(shaxarlar1['Samarqand'])

# 2 masala

# print('Xiva' in shaxarlar1)
# print(550 in shaxarlar1.values)


# 3 masala

shaxarlar1.name = 'Aholi'
shaxarlar1.index.name = 'Shaxar'

# print(shaxarlar1)

# 4 masala

filial_a = {'non': 50, 'sut': 30, 'yog': 10}
filial_b = {'non': 40, 'sut': 20, 'tuxum': 60}


filial_a1 = Series(filial_a)
filial_b1 = Series(filial_b)

jami = filial_a1.add(filial_b1, fill_value=0)
nan = jami[jami.isnull()]

# print(jami)


#5 masala

ismlar = {'Ali': 80, 'Vali': 55, 'Sardor': 70}

ismlar1 = Series(ismlar)

model = ['Ali', 'Vali', 'Sardor', 'Dilnoza']

ismlar2 = Series(ismlar, index= model)
# print(ismlar2)

# print(ismlar2.isnull().sum())

# 6 maasala

cars_vocab = {
    'Malibu':40000,'Lacetti':20000,'Toyota':45000,
    'Mazda':52000, 'Honda':38000
    }

cars1 = Series(cars_vocab)

qimmat = cars1.idxmax()
arzon = cars1.idxmin()


# print(f"Eng qimmat mashina {cars1[qimmat]}")
# print(f"Eng arzon mashina {cars1[arzon]}")
# print(f"Farqi {cars1[qimmat] - cars1 [arzon]}")


# 7 masala

qimmatlari = cars1[cars1 >= 40000]
# print(qimmatlari.sort_values(ascending=False))


# 8 masala

ranglar  = ['qora', 'oq', 'qora', 'qizil', 'oq', 'qora', 'oq', 'oq']

rangs = Series(ranglar)
hisob = rangs.value_counts()

# print(hisob.idxmax())
# print(hisob.max())

# 9 masala

baholar = {'A': 100, 'B': None, 'C': 300, 'D': None}
bahoS = Series(baholar)

orta_baho = bahoS.mean()

tushish = bahoS.dropna()

toldirish = bahoS.fillna(orta_baho)

# print(bahoS)
# print(orta_baho)
# print(tushish)

# print(toldirish)

# 10 masala

mahsulot = {'a': 10, 'b': 25, 'c': 40, 'd': 15}
mahsulots = Series(mahsulot)

ortacha = mahsulots.mean()

kichik = mahsulots[mahsulots < ortacha]
print(list(kichik.index))

















