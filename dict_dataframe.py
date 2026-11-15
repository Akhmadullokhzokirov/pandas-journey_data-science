"""
Pandas: DataFrame, ustunlar va lug'atdan DataFrame yaratish

Tarkibi:
    1-qism      DataFrame yaratish va ustunlar bilan ishlash
    2-qism      Ichma-ich lug'atdan DataFrame yaratish
    1-9 masala  Mustahkamlash uchun masalalar

Har bir "# %%" qismi alohida ishga tushadi (Spyder / VS Code / Jupyter).
"""

# %% 1-qism: DataFrame yaratish va ustunlar bilan ishlash
import pandas as pd

data = {
    'Yil': [2021, 2020, 2019, 2018, 2017, 2016, 2015, 2010],
    'Aholi soni': [33.9, 33.5, 32.9, 32.5, 31.9, 31.4, 30.9, 28.5],
    'Temp': [1.54, 1.48, 1.56, 1.62, 1.65, 1.66, 1.64, 1.53]
}

# columns= ustunlar tartibini belgilaydi.
# Lug'atda yo'q ustun (YAIM) NaN bilan to'ladi.
df = pd.DataFrame(
    data,
    columns=['Yil', 'Temp', 'Aholi soni', 'YAIM'],
    index=[31, 32, 33, 34, 35, 36, 37, 38]
)
print(df)
print(df.head(6))   # boshidagi 6 qator, raqam berilmasa 5 qator
print(df.shape)     # (qatorlar soni, ustunlar soni)

# Ustunni tanlash: har bir ustun Series
aholi = df['Aholi soni']
print(aholi)
print(type(aholi))
print(df.Temp)      # nuqta bilan faqat nomida bo'sh joy bo'lmasa ishlaydi

# Yozishda doim df['nom'] ishlatamiz
df['YAIM'] = 0
print(df)

# Series bilan tayinlash: INDEKS YORLIG'I bo'yicha moslashadi,
# mos kelmagan qatorlar NaN bo'ladi (ustun float64 ga o'tadi)
val = pd.Series([1700, 1650, 1600], index=[31, 33, 35])
df['YAIM'] = val
print(df)

# Ro'yxat bilan tayinlash: TARTIB bo'yicha joylanadi, uzunlik teng bo'lishi shart
val = [2000, 1950, 1900, 1850, 1800, 1750, 1700, 1500]
df['YAIM'] = val
print(df)

# Mantiqiy ifoda bilan yangi (True/False) ustun
df['1800+'] = df['YAIM'] > 1800
print(df)

# Ustunni o'chirish (joyida)
del df['1800+']
print(df)


# %% 2-qism: Ichma-ich lug'atdan DataFrame yaratish
import pandas as pd

# Tashqi kalit = ustun, ichki kalit = indeks
data = {
    'Uzbekistan': {2021: 33.9, 2020: 33.5, 2019: 32.9, 2018: 32.5, 2017: 31.5},
    'Kazahistan': {2021: 18.9, 2020: 18.7, 2019: 18.5, 2018: 18.3, 2017: 18.1, 2016: 18.8}
}

df = pd.DataFrame(data)   # Uzbekistan'da 2016 yo'q -> NaN
print(df)

df.index.name = 'Yil'
print(df)

df = pd.DataFrame(data, index=[2021, 2019, 2017])   # faqat tanlangan qatorlar
print(df)

print(df.T)   # transpozitsiya: qator va ustunlar almashadi

arr = df.values   # NumPy massivi (yorliqlar yo'qoladi)
print(arr)
print(type(arr))


# %% 1-masala: Do'kon (lug'atdan DataFrame)
# Qoida: kalit = ustun nomi, qiymat = shu ustunning barcha qiymatlari (ro'yxat)
import pandas as pd

mahsulotlar = {
    'Mahsulot': ['Non', 'Sut', 'Tuxum', "Yog'", 'Shakar'],
    'Narx': [5000, 12000, 18000, 30000, 14000],
    'Soni': [40, 25, 30, 10, 0]
}

df = pd.DataFrame(mahsulotlar, index=[101, 102, 103, 104, 105])
print(df)
print(df.head(3))
print(df.shape)   # (5, 3)


# %% 2-masala: Yangi ustunlar
df['Jami'] = df['Narx'] * df['Soni']
df['Mavjud'] = df['Soni'] > 0   # masalada nima so'ralsa, aynan shuni tekshiramiz
print(df)

# Ikki ustunni tanlashda qavs ikkita: natija DataFrame bo'ladi
yangi = df[['Mahsulot', 'Jami']].copy()   # .copy() mustaqil nusxa beradi
print(yangi)


# %% 3-masala: columns= parametri
# Natija: faqat C va A (shu tartibda) va yangi D ustuni (NaN).
# 'B' lug'atda bor, lekin columns ro'yxatida yo'q, shuning uchun tashlab yuboriladi.
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data, columns=['C', 'A', 'D'])
print(df)


# %% 4-masala: Series va ro'yxat bilan tayinlash
df = pd.DataFrame({'Ism': ['Ali', 'Vali', 'Gulnora', 'Sardor']},
                  index=[10, 20, 30, 40])
print(df)

# Series: yorliq bo'yicha. 20 va 40 -> NaN, 50 yorlig'i df'da yo'q (tashlanadi)
ball = pd.Series([90, 75, 88], index=[10, 30, 50])
df['Ball'] = ball
print(df)
print(df['Ball'].dtype)   # float64 (NaN float turiga kiradi)

# Ro'yxat: tartib bo'yicha, uzunlik mos kelmasa ValueError
try:
    df['Ball'] = [90, 75, 88]
except ValueError as xato:
    print('ValueError:', xato)

# Series ichidagi tartib ahamiyatsiz, ro'yxatda esa tartib hal qiladi
df = pd.DataFrame({'Ism': ['Ali', 'Vali', 'Gulnora']}, index=[1, 2, 3])
df['A'] = pd.Series([10, 20, 30], index=[3, 2, 1])   # yorliq bo'yicha -> 30, 20, 10
df['B'] = [10, 20, 30]                                # tartib bo'yicha -> 10, 20, 30
print(df)


# %% 5-masala: Shaharlar harorati (ichma-ich lug'at)
xarorat = {
    'Toshkent': {2022: 15.2, 2023: 15.8, 2024: 16.1},
    'Samarqand': {2022: 14.1, 2023: 14.6},
    'Buxoro': {2023: 16.0, 2024: 16.5}
}

df = pd.DataFrame(xarorat)   # oxirida vergul yo'q, aks holda tuple bo'ladi!
df.index.name = 'Yil'
print(df)   # NaN: Samarqand-2024 va Buxoro-2022 (ma'lumot yo'q)
print(df.T)   # shaharlar qatorga, yillar ustunga aylandi


# %% 6-masala: Ustunlarni boshqarish
# rename va drop yangi obyekt qaytaradi: natijani saqlash kerak
df = pd.DataFrame(xarorat)
df.index.name = 'Yil'

df = df.rename(columns={'Toshkent': 'Tosh'})
print(df)

df['Namangan'] = 13.5      # bitta qiymat barcha qatorga takrorlanadi
print(df)

del df['Samarqand']        # Python buyrug'i, joyida o'chiradi
print(df)

df = df.drop(columns='Namangan')   # DataFrame metodi, yangi obyekt qaytaradi
print(df)

print(list(df.columns))    # ['Tosh', 'Buxoro']


# %% 7-masala: values va tiplar
df = pd.DataFrame(xarorat)
df.index.name = 'Yil'

arr = df.values
print(arr)
print(type(arr))     # numpy.ndarray
print(arr.shape)     # (3, 3)
print(arr.dtype)     # float64

# Matnli ustun qo'shilsa: NumPy massivida bitta tur bo'lishi kerak,
# shuning uchun hammasi object ga o'tadi (xato chiqmaydi)
df['Andijon'] = ['Eski shahar', 'Chinor', 'Uzumzor']
print(df.values.dtype)   # object (butun massiv uchun bitta tur)
print(df.dtypes)         # har ustunning o'z turi


# %% 8-masala: Mantiqiy filtrlash
mahsulotlar = {
    'Mahsulot': ['Non', 'Sut', 'Tuxum', "Yog'", 'Shakar'],
    'Narx': [5000, 12000, 18000, 30000, 14000],
    'Soni': [40, 25, 30, 10, 0]
}
df = pd.DataFrame(mahsulotlar, index=[101, 102, 103, 104, 105])

m1 = df['Narx'] > 10000
m2 = df['Soni'] < 20
m3 = df['Narx'] < 10000
m4 = df['Soni'] == 0

print(df[m1 & m2])   # narxi > 10000 VA soni < 20 -> Yog', Shakar
print(df[m3 | m4])   # narxi < 10000 YOKI soni == 0 -> Non, Shakar

# Qavs shart: & ning ustuvorligi > va < dan yuqori.
# df[df.Narx > 10000 & df.Soni < 20] -> ValueError (Series'ning chinligi noaniq)
print(df[(df['Narx'] > 10000) & (df['Soni'] < 20)])   # to'g'ri yozilishi


# %% 9-masala: NaN bilan ishlash
data = {
    'Ism': ['Ali', 'Vali', 'Gulnora', 'Sardor', 'Dilnoza'],
    'Yosh': [25, None, 30, None, 28],
    'Maosh': [500, 600, None, 450, 700]
}
df = pd.DataFrame(data)

print(df.isna().sum())   # Yosh: 2, Maosh: 1

# dropna ni to'ldirishdan OLDIN, alohida nusxada qo'llaymiz
toza = df.dropna()
print(toza)   # faqat Ali va Dilnoza qoladi

# fillna yangi obyekt qaytaradi, shuning uchun qayta tayinlaymiz
df['Maosh'] = df['Maosh'].fillna(0)
df['Yosh'] = df['Yosh'].fillna(df['Yosh'].mean())   # (25 + 30 + 28) / 3
print(df)

# Yosh ustuni float: NaN float turiga kiradi, int uni saqlay olmaydi
print(df.dtypes)