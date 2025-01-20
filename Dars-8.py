# -*- coding: utf-8 -*-
"""
15/01/2025

Dasturlash asoslari. Amaliot.

#08-dars: RO'YXAT BILAN ISHLASH

Bajardi: Roma Jek

Web sahifa: https://python.sariq.dev

"""

# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
countries = ['Uzbekistan', 'Kazakastan', 'Azerbaijan', 'United States of America', 'United Kingdom', 'China', 'Korea', 'Japan']
print(countries)



# Ro'yxatning uzunligini konsolga chiqaring
print(len(countries))



# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(countries))



# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(countries, reverse=True))



# Asl ro'yxatni qaytadan konsolga chiqaring
print(countries)



# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
countries.reverse()
print(countries)



# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha,
countries.sort()
print(countries)
#  keyin esa alifboga teskari tartibda konsolga chiqaring.
countries.sort(reverse=True)
print(countries)



# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
juft_list = list(range(120, 1200, 2))
print(juft_list)


# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print(sum(juft_list))



# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
print("max-min = ", max(juft_list) - min(juft_list))



# Ro'yxatdagi elementlar sonini hisoblang
print(len(juft_list))



# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(juft_list[:20]) # boshidan 0...19 indexgacha 20 element chiqdi
print(juft_list[ (len(juft_list)//2-10) : (len(juft_list)//2+10) ] ) # o'rtasidan
print( juft_list[ (len(juft_list)-20 ) : ] ) # o'xiridan
# Amaliot mashqi emeas. Listni o'rtasinji elementlar kesib olishni tushinishga misol uchun ishlandi.
# pak = list(range(9))
# print(pak)
# print(len(pak)//2)
# print(pak[ (len(pak)//2 - 1) : (len(pak)//2 + 1)])



# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ["sho'rva", "choy", "osh", "kabob", "ko'k choy"] 



# nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushda = taomlar[:]



# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushda.remove("sho'rva")
nonushda.remove("osh")
nonushda.remove("kabob")
nonushda.append("saryog'")
nonushda.append("asal")



# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar)
print(nonushda)



# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushda = tuple(nonushda)
# nonushda[0] = "qaymoq va non"  # element qo'shilmadi, sababi bu o'zgartirib bo'lmas ro'yxat



