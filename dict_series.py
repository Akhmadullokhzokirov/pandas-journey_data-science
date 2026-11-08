"""
Pandas Series: lug'atdan yaratish va asosiy metodlar

Mavzular:
    1. Lug'atdan Series yaratish (index= bilan tanlash)
    2. `in` operatori: indeks nomi va qiymat farqi
    3. NaN bilan ishlash: isnull, notnull, dropna, fillna
    4. Indeks bo'yicha moslashish: + va add(fill_value=0)
    5. name va index.name
    6. Metodlar: idxmax, idxmin, max, min, mean, sum,
                 sort_values, value_counts
    7. Filtrlash va list(index)

Bo'limlar oxirida "Mashq" bo'limida 10 ta masalaning yechimi berilgan.
"""

import pandas as pd
from pandas import Series


# ===========================================================================
# 1. Lug'atdan Series yaratish
# ===========================================================================
cars_vocab = {
    'Malibu': 40000, 'Lacetti': 20000, 'Toyota': 45000,
    'Mazda': 52000, 'Honda': 38000,
}

# 1-usul: tayyor lug'atni berish. Kalitlar indeks, qiymatlar Series qiymati.
cars1 = Series(cars_vocab)
print(type(cars1))
print(cars1)

# 2-usul: lug'atni to'g'ridan-to'g'ri Series ichiga yozish
cars2 = Series({
    'Malibu': 40000, 'Lacetti': 20000, 'Toyota': 45000,
    'Mazda': 52000, 'Honda': 38000,
})

# index= bilan tanlash va tartiblash. Lug'atda yo'q nom (Jaguar) uchun NaN chiqadi.
models = ['Honda', 'Mazda', 'Lacetti', 'Jaguar', 'Malibu', 'Toyota']
cars3 = Series(cars_vocab, index=models)
print(cars3)   # Jaguar: NaN, qiymatlar float bo'lib qoladi


# ===========================================================================
# 2. `in` operatori
# ===========================================================================
# `in` faqat INDEKS NOMLARI orasidan qidiradi
print('Malibu' in cars2)           # True
print(cars2['Toyota'])             # 45000

# Qiymat orasidan qidirish uchun .values kerak
print(40000 in cars2)              # False (40000 nom emas)
print(40000 in cars2.values)       # True


# ===========================================================================
# 3. NaN bilan ishlash
# ===========================================================================
print(cars3.isnull())              # NaN bo'lsa True
print(cars3.notnull())             # NaN bo'lmasa True

# isnull() natijasidagi True ni 1 deb sanaydi, shuning uchun .sum() NaN sonini beradi
print(cars3.isnull().sum())        # 1


# ===========================================================================
# 4. Indeks bo'yicha moslashish
# ===========================================================================
# Qo'shish indeks NOMI bo'yicha moslanadi, tartib bo'yicha emas
print(cars1 + cars2)               # indekslar bir xil, narxlar ikki baravar

# Faqat bittasida bor nom uchun NaN chiqadi. add() va fill_value=0 NaN ni oldini oladi
a = Series({'x': 1, 'y': 2})
b = Series({'y': 10, 'z': 20})
print(a + b)                       # x: NaN, y: 12, z: NaN
print(a.add(b, fill_value=0))      # x: 1, y: 12, z: 20


# ===========================================================================
# 5. name va index.name
# ===========================================================================
cars2.name = 'Avtosalon'           # Seriesning nomi
cars2.index.name = 'Modellar'      # indeksning nomi
print(cars2)


# ===========================================================================
# MASHQ: 10 ta masala
# ===========================================================================

# --- 1-masala: lug'atdan Series yaratish va nom bo'yicha olish --------------
shaxarlar = {'Toshkent': 2800, 'Samarqand': 550, 'Buxoro': 280}
shaxarlar1 = Series(shaxarlar)
print(shaxarlar1)
print(shaxarlar1['Samarqand'])


# --- 2-masala: `in` operatori (nom va qiymat) -------------------------------
print('Xiva' in shaxarlar1)            # False (nom bo'yicha)
print(550 in shaxarlar1)               # False (qiymat emas, nom izlaydi)
print(550 in shaxarlar1.values)        # True  (qiymat bo'yicha)
print(999 in shaxarlar1.values)        # False


# --- 3-masala: name va index.name -------------------------------------------
shaxarlar1.name = 'Aholi'
shaxarlar1.index.name = 'Shaxar'
print(shaxarlar1)


# --- 4-masala: moslashish, NaN va add(fill_value=0) -------------------------
filial_a = {'non': 50, 'sut': 30, 'yog': 10}
filial_b = {'non': 40, 'sut': 20, 'tuxum': 60}

filial_a1 = Series(filial_a)
filial_b1 = Series(filial_b)

yigindi = filial_a1 + filial_b1
print(yigindi)                              # tuxum va yog: NaN
print(yigindi[yigindi.isnull()])            # faqat bitta filialda borlar

jami = filial_a1.add(filial_b1, fill_value=0)
print(jami)                                 # NaN yo'q, to'liq yig'indi


# --- 5-masala: index= bilan lug'atdan Series, NaN sonini sanash --------------
ismlar = {'Ali': 80, 'Vali': 55, 'Sardor': 70}
model = ['Ali', 'Vali', 'Sardor', 'Dilnoza']   # Dilnoza lug'atda yo'q

ismlar2 = Series(ismlar, index=model)
print(ismlar2)
print(ismlar2.isnull())
print(ismlar2.isnull().sum())                  # 1


# --- 6-masala: idxmax, idxmin, farq -----------------------------------------
# idxmax/idxmin NOM qaytaradi, narxni nom orqali olamiz
qimmat = cars1.idxmax()
arzon = cars1.idxmin()
farq = cars1[qimmat] - cars1[arzon]

print(f"Eng qimmat mashina {qimmat}: {cars1[qimmat]}")
print(f"Eng arzon mashina {arzon}: {cars1[arzon]}")
print(f"Narx farqi: {farq}")


# --- 7-masala: filtr + kamayish tartibida saralash --------------------------
qimmatlar = cars1[cars1 >= 40000]                # 40000 ning o'zi ham kiradi
print(qimmatlar.sort_values(ascending=False))    # kamayish tartibida


# --- 8-masala: value_counts ---------------------------------------------------
ranglar = ['qora', 'oq', 'qora', 'qizil', 'oq', 'qora', 'oq', 'oq']
rangs = Series(ranglar)

hisob = rangs.value_counts()      # har bir rang necha marta uchraydi
print(hisob)
print(hisob.idxmax())             # eng ko'p uchraydigan rang: oq
print(hisob.max())                # necha marta: 4


# --- 9-masala: dropna, fillna, mean ------------------------------------------
baholar = {'A': 100, 'B': None, 'C': 300, 'D': None}
bahoS = Series(baholar)

orta_baho = bahoS.mean()          # NaN larni o'tkazib yuboradi: (100 + 300) / 2
tushish = bahoS.dropna()          # NaN lar olib tashlanadi (yangi Series)
toldirish = bahoS.fillna(orta_baho)   # NaN lar o'rtacha bilan to'ldiriladi

print(orta_baho)                  # 200.0
print(tushish)
print(toldirish)


# --- 10-masala: o'rtachadan past narxli mahsulotlar ro'yxati -----------------
mahsulot = {'a': 10, 'b': 25, 'c': 40, 'd': 15}
mahsulots = Series(mahsulot)

ortacha = mahsulots.mean()                     # 22.5, qo'lda yozilmaydi

kichik = mahsulots[mahsulots < ortacha]        # filtr
print(list(kichik.index))                      # ['a', 'd']