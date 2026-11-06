"""
Pandas Series asoslari

Mavzular:
    1. Series yaratish (standart indeks bilan)
    2. .values va .index
    3. Maxsus (matnli) indeks bilan Series
    4. Indeks bo'yicha elementlarni olish
    5. Shart bo'yicha filtrlash (bool indekslash)
    6. Vektorlashgan amallar va NumPy funksiyalari
"""

import numpy as np
from pandas import Series


# ---------------------------------------------------------------------------
# 1. Standart indeksli Series
# ---------------------------------------------------------------------------
# Indeks berilmasa, pandas avtomatik 0, 1, 2, ... indeksini qo'yadi.
obj = Series([4, 5, 6, -6.5])

print(type(obj))   # <class 'pandas.core.series.Series'>
print(obj)


# ---------------------------------------------------------------------------
# 2. Qiymatlar va indeks
# ---------------------------------------------------------------------------
print(obj.values)  # qiymatlar (aslida NumPy massivi)
print(obj.index)   # indeks (bu yerda RangeIndex)

# Indeks raqam bo'lgani uchun, obj[0] nomi 0 bo'lgan elementni qaytaradi
print(obj[0])


# ---------------------------------------------------------------------------
# 3. Maxsus indeksli Series
# ---------------------------------------------------------------------------
# Har bir qiymatga matnli nom (yorliq) beramiz.
obj2 = Series([6, 3, 2, 1], index=['a', 'b', 'c', 'd'])

print(obj2)
print(obj2.index)


# ---------------------------------------------------------------------------
# 4. Elementlarni olish
# ---------------------------------------------------------------------------
# Bitta element: nom bo'yicha
print(obj2['a'])

# Bir nechta element: ro'yxat beriladi (ikki qavs: tashqi = indekslash,
# ichki = nomlar ro'yxati). Natija yangi Series bo'ladi.
print(obj2[['a', 'c', 'd']])

# Pozitsiya (tartib raqami) bo'yicha olish uchun .iloc ishlatiladi
print(obj2.iloc[0])


# ---------------------------------------------------------------------------
# 5. Shart bo'yicha filtrlash
# ---------------------------------------------------------------------------
# Taqqoslash har bir elementga qo'llanadi va bool Series qaytaradi
print(obj2 < 3)

# Bool Seriesni indeks sifatida berib, faqat True bo'lganlarni olamiz
print(obj2[obj2 < 3])


# ---------------------------------------------------------------------------
# 6. Vektorlashgan amallar
# ---------------------------------------------------------------------------
# Amal barcha elementga birdaniga qo'llanadi (tsikl kerak emas).
# Natija yangi Series, asl obj2 o'zgarmaydi.
print(obj2 * 2)
print(obj2)        # hali ham 6, 3, 2, 1

# NumPy funksiyalari ham Series bilan ishlaydi, indeks saqlanadi
print(np.exp(obj2))