"""
15/01/2025

Dasturlash asoslari. Amaliot.

#12-dars: XATOLAR BILAN ISHLASH

Bajardi: Jalgasov Ramazan

Web sahifa: https://python.sariq.dev

"""


son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")