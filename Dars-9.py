# -*- coding: utf-8 -*-
"""
15/01/2025

Dasturlash asoslari. Amaliot.

#09-dars: FOR TAKRORLASH OPERATORI

Bajardi: Roma Jek

Web sahifa: https://python.sariq.dev

"""


# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olin'] 
for n in ismlar:
    print(f"Salom {n}")



# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring 
# (n o'rniga kod necha marta takrorlanganini yozing)
print(f"Kod {len(ismlar)} marta takrorlandi ")



# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini
# yangi qatordan konsolga chiqaring.
toq_sonlar = list(range(11, 100, 2))
for n in toq_sonlar:
    print(n**3)



# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga 
# saqlab oling. Natijani konsolga chiqaring.
kinolar = []
for k in range(5):
    kinolar.append(input(f"{k+1}- sevimli kino: ").strip().lower())
print(kinolar)



# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir
# suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
h = int(input("Bugun nechta odam bilan suhbatlashding: "))
suhbatlar = []
for m in range(h):
    suhbatlar.append(input(f"{m+1} chi suhbat odam kim:").strip().title())
print(suhbatlar)
    
    




