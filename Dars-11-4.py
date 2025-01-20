# -*- coding: utf-8 -*-
"""
15/01/2025

Dasturlash asoslari. Amaliot.

#11-dars: BIR NECHTA SHARTLARNI TEKSHIRISH

Bajardi: Roma Jek

Web sahifa: https://python.sariq.dev

"""


# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan
# bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. 
# Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa 
# "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.



mahsulotlar = ["uzum", "olma", "kalbasa", "saryoq", "kapusta", "kola", "non", "osh qovoq", "tuqum", "banan"]
savat = []

for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: ").strip().lower())

for mah in savat:
    if mah in mahsulotlar:
        print(f"Do'konimizda {mah} bor")
    else:
        print(f"Do'konimizda {mah} yo'q")
























