# -*- coding: utf-8 -*-

"""
15/01/2025

Dasturlash asoslari. Amaliot.

#11-dars: BIR NECHTA SHARTLARNI TEKSHIRISH

Bajardi: Roma Jek

Web sahifa: https://python.sariq.dev

"""

# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. 
# Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda 
# yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa,
# "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar
# do'konimizda yo'q: ....." degan xabarni chiqaring.



mahsulotlar = ["uzum", "olma", "kalbasa", "saryoq", "kapusta", "kola", "non", "osh qovoq", "tuqum", "banan"]
bor_mahsulotlar =[]
mavjud_emas = []

for n in range(5):
    mahsulot = input(f"Savatga {n+1}- mahsulotni kiriting: ").strip().lower()
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print("Do'konimizda quyidagi mahsulotlar yo'q:")
    for yoq_mahsulot in mavjud_emas:
        print(yoq_mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
















