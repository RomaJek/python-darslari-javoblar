
"""
15/01/2025

Dasturlash asoslari. Amaliot.

#05-dars: STRING (MATN)

Bajardi: Roma Jek

Web sahifa: https://python.sariq.dev

"""





# Quyidagi o'zgaruvchilarni yarating: 
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor" 
viloyat = "Samarqand"



# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")



# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang.
# Va avvalgi mashqni takrorlang.
kocha=input("ko'cha: ").strip().title()
mahalla=input("mahalla: ").strip().title()
tuman=input("tuman: ").strip().title()
viloyat=input("viloyat: ").strip().title()

print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")



# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
print(f"{kocha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati")



# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)



# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini 
# qo'llab ko'ring.
print(manzil.title())
print(manzil.upper())
print(manzil.lower())
print(manzil.capitalize())


