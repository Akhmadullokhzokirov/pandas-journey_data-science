"""
Pandas Index metodlari: difference, union, delete, drop.

Mavzu: ikkita DataFrame ni birlashtirish (concat) va Index obyekti bilan ishlash.
"""

import pandas as pd

# 1. Ma'lumotlarni tayyorlash

usernames = {
    "anvar": "anvarbek223",
    "olim": "olimtoy",
    "maryam": "maryam223344",
    "javohir": "javohir445",
}

emails = {
    "anvar": "anvar@gmail.com",
    "olim": "olim@mail.ru",
    "maryam": "maryam@gmail.com",
    "javohir": "javohir445@gmail.com",
}

df = pd.DataFrame({"username": usernames, "email": emails})
print("df:\n", df, "\n")

# 2. Yangi ma'lumotlar va concat

data2 = {
    "username": {"abdullo": "abdullo21", "maryam": "maryam2001"},
    "email": {"abdullo": "abdullo21@gmail.com", "maryam": "maryam01@gmail.com"},
}
new_df = pd.DataFrame(data2)

df2 = pd.concat([df, new_df])
print("df2 (concat):\n", df2, "\n")
print("Index takrorlanyaptimi?", not df2.index.is_unique, "\n")

# 3. Index metodlari

new_idx = pd.Index(["olim", "nafisa", "hamida"])
print("new_idx:", new_idx.tolist())

# difference: df2 da bor, new_idx da yo'q
print("difference:", df2.index.difference(new_idx).tolist())

# union: ikkalasining birlashmasi (takrorlarsiz, saralangan)
print("union:", df2.index.union(new_idx).tolist())

# delete: pozitsiya (raqam) bo'yicha o'chirish
print("delete(1):", new_idx.delete(1).tolist())

# drop: qiymat (label) bo'yicha o'chirish
print("drop('hamida'):", new_idx.drop("hamida").tolist())

# Index o'zgarmas (immutable): asl new_idx o'zgarmaydi
print("asl new_idx:", new_idx.tolist())