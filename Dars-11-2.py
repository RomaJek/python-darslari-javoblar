# -*- coding: utf-8 -*-
"""
15/01/2025

Dasturlash asoslari. Amaliot.

#11-dars: BIR NECHTA SHARTLARNI TEKSHIRISH

Bajardi: Roma Jek

Web sahifa: https://python.sariq.dev

"""

# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:

# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

yosh = int(input("Yoshingiz nechda? "))
narh = 0
if yosh > 0:
    if yosh <= 4 or 60 < yosh:
        narh = 0
    elif yosh < 18:
        narh = 10000
    else:
        narh = 20000
    print(f"Chipta narhi {narh} so'm")
else:
    print("Yosh 0 dan katta bo'ladi")

        













