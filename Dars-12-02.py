"""
15/01/2025

Dasturlash asoslari. Amaliot.

#12-dars: XATOLAR BILAN ISHLASH

Bajardi: Jalgasov Ramazan

Web sahifa: https://python.sariq.dev

"""

yosh = int(input("Yoshingiz nechida?"))

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")
