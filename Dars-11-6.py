# -*- coding: utf-8 -*-
"""
15/01/2025

Dasturlash asoslari. Amaliot.

#11-dars: BIR NECHTA SHARTLARNI TEKSHIRISH

Bajardi: Roma Jek

Web sahifa: https://python.sariq.dev

"""




# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi
# login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi
# bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks
# holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.


foydalanuvchilar = ["aziz", "kimju", "sasha", "kamol22", "malika99"]

login = input("Yangi login tanlang: ").strip().lower()
if login in foydalanuvchilar:
    print("Login band yangi login tanlang!")
else:
    print("Xush kelibsiz, foydalanuvchi!")
    foydalanuvchilar.append(login)











