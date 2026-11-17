"""
Mini loyiha: Xodimlar jadvali (Pandas)

Maqsad: DataFrame mavzusidagi tushunchalarni bitta kichik loyihada birlashtirish:
lug'atdan DataFrame yaratish, set_index, shartli ustun (np.where),
filtrlash, info/describe va sort_values.
"""

import numpy as np
import pandas as pd

# ---------------------------------------------------------------
# 0. Ma'lumot: 6 xodim, 3 bo'lim (ba'zi xodimlar bir bo'limda)
# ---------------------------------------------------------------
xodimlar = {
    'Ism': ['Ali', 'Hasan', 'Husan', 'Abdulloh', 'Qosim', 'Sardor'],
    'Bolim': ['Savdo', 'Savdo', 'Ombor', 'Ombor', 'Buxgalteriya', 'Savdo'],
    'Maosh': [5000, 7000, 9000, 10000, 15000, 6000],
    'Tajriba': [1, 2, 3, 4, 5, 7]
}
df = pd.DataFrame(xodimlar)

# ---------------------------------------------------------------
# 1. Ism ustunini indeksga aylantiramiz
#    set_index yangi DataFrame qaytaradi, shuning uchun natijani saqlaymiz
# ---------------------------------------------------------------
df = df.set_index('Ism')

# ---------------------------------------------------------------
# 2. Shartli ustun: tajriba 3 yildan KO'P bo'lsa maosh x1.2, aks holda x1.1
#    Husan (aynan 3 yil) x1.1 oladi, chunki shart qat'iy ">" .
# ---------------------------------------------------------------
df['Maosh_oshirilgan'] = np.where(
    df['Tajriba'] > 3,
    df['Maosh'] * 1.2,
    df['Maosh'] * 1.1
)
print('--- 2. Maosh oshirilgandan keyin ---')
print(df)

# ---------------------------------------------------------------
# 3. O'rtachadan yuqori maosh olgan xodimlar
#    Avval o'rtachani alohida hisoblaymiz, keyin mask bilan filtrlaymiz
# ---------------------------------------------------------------
orta_maosh = df['Maosh'].mean()
yuqori_maosh = df[df['Maosh'] > orta_maosh]
print('\n--- 3. O\'rtacha maosh:', round(orta_maosh, 2), '---')
print(yuqori_maosh)   # Husan, Abdulloh, Qosim

# ---------------------------------------------------------------
# 4. info() va describe()
#    info() natijani o'zi chop etadi (None qaytaradi), print(...) kerak emas
# ---------------------------------------------------------------
print('\n--- 4. info() ---')
df.info()
print('\n--- 4. describe() ---')
print(df.describe())

# Kuzatuvlar (Maosh ustuni bo'yicha):
# 1) O'rtacha maosh (8666.67) mediana (8000) dan yuqori. Sabab: Qosimning
#    maoshi (15000) boshqalardan ancha katta va o'rtachani yuqoriga tortadi.
#    Bunday ma'lumotda mediana oddiy xodim maoshini yaxshiroq ko'rsatadi.
# 2) Eng yuqori maosh (15000) eng pastdan (5000) 3 marta katta:
#    maoshlar orasidagi farq katta.
# 3) Maosh oshirilgandan keyin o'rtacha maosh 8666.67 dan 10050 ga ko'tariladi,
#    ya'ni xarajat taxminan 16% ga oshadi.
oshish = df['Maosh_oshirilgan'].mean() / df['Maosh'].mean()
print('\nO\'rtacha maosh oshishi:', round((oshish - 1) * 100, 1), '%')

# ---------------------------------------------------------------
# 5. Saralash: sort_values yangi obyekt qaytaradi, asl df o'zgarmaydi
# ---------------------------------------------------------------
print('\n--- 5. Bolim bo\'yicha ---')
print(df.sort_values('Bolim'))

print('\n--- 5. Bolim, keyin Maosh bo\'yicha ---')
print(df.sort_values(['Bolim', 'Maosh']))

print('\n--- 5. Maosh kamayish tartibida ---')
print(df.sort_values('Maosh', ascending=False))