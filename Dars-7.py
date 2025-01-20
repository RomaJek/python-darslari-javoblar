# -*- coding: utf-8 -*-
"""
15/01/2025

Dasturlash asoslari. Amaliot.

#07-dars: Lists

Bajardi: Roma Jek

Web sahifa: https://python.sariq.dev

"""

    
# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar = ['Roma', 'Jasarat', 'Aziz']
print(ismlar[0], " ishlar yaqshimi")
print(f"{ismlar[1]} bugun darsga borasmi?")
print(ismlar[-1] + " ishga borasizmi?")



# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
sonlar = [1, 2, 2.3, -3, -3.2, 0.1, -0.2]



# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring.
# Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
sonlar = [1, 2, 2.3, -3, -3.2, 0.1, -0.2]
print(sonlar[0] - sonlar[-1]) 
print(len(sonlar))
print(sonlar)
sonlar.append( sonlar[0] - sonlar[1] ) # list oxiriga element qoshdik
print(sonlar)
sonlar.pop() # Listning oxiridagi elementini sug'irib oldi. index berilmagani uchun
print(sonlar)
del sonlar[len(sonlar)-1]  # List ning oxirgi indexini berib. shu elementni o'chirdik
print(sonlar)

# 1-List elementlarini almashdirishga misol
just = sonlar[1]
sonlar[1] = sonlar[2]
sonlar[2] = just
print(sonlar)  # List ning 1 va 2 elementlari o'rnini almashtirdik.

# 2-List elementlarini almashdirishga misol
sonlar.append(sonlar[1]) # 1 indexdagi element List oxiriga copy qilib oldik
print(sonlar)
sonlar[1] = sonlar[2]
sonlar[2] = sonlar[len(sonlar) - 1]
sonlar.pop() # List ning oxirgi elementini sug'irib oldik
print(sonlar)



# t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan 
# tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 
t_shaxslar = ['Bobur', 'Ibrayim', 'Navoiy']
z_shaxslar = ['Bill Geyst', 'Mark Zukerberg', 'Mask']



# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), 
# quyidagi ko'rinishda chiqaring:
print("Men tarixiy shaxslardan", t_shaxslar.pop(1), "bilan, zamonaviy shaxslardan esa",
      z_shaxslar.pop(2), "bilan suhbat qilishni istar edim")



# friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi
# bo'lgan do'stlaringizni kiriting. 
friends = []
friends.append("Sardor")
friends.append("Ilhom")
friends.append("Roma")
friends.append("Malik")
friends.append("Jasur")
print(friends)



# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida
#  o'chrib tashlang. 
friends.remove("Sardor")
friends.remove("Malik")
print(friends)



# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.insert(0, "Jek")
friends.append("Maykl")
friends.insert(len(friends)//2, "Tom")
print(friends)



# Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida
# mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop())
print("\nDo'stlar: ", friends)
print("Kelgan mehmonlar: ", mehmonlar)


















