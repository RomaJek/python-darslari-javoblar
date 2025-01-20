# -*- coding: utf-8 -*-
"""
15/01/2025

Dasturlash asoslari. Amaliot.

#11-dars: BIR NECHTA SHARTLARNI TEKSHIRISH

Bajardi: Roma Jek

Web sahifa: https://python.sariq.dev

"""



# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha 
# bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 

son = int(input("Istalgan butun son kiriting: "))

for n in range(2, 11, 1):
    if son%n == 0:
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

























