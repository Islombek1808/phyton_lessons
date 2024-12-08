# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 20:32:20 2024

@author: iBro_SERVICE
"""

# if OPERATORI   # if OPERATORI  # if OPERATORI# if OPERATORI   # if OPERATORI  # if OPERATORI


'''
avtolar=['audi', 'bmw', 'volvo', 'kia', 'hyundai']
for avto in avtolar:
    if avto=='bmw':
        print(avto.upper())
    else:
        print(avto.title())
'''

'''
ismlar='Ali'
ismlar=ismlar.upper()
'''   

'''
# QIYMATLARNING TENG EMASLIGINI SOLISHTIRISH
ism=input('Ismingiz nima\n>')       #   != TENG EMASMI BELGISI     == TENGMI BELGISI
if ism.lower()!='ali':
    print(f"uzr, {ism.title()} biz Alini kutyapmiz")
else:
    print("salom Ali")

# SONLARNI SOLISHTIRISH
'''
'''

javob=float(input("12*6 nechaga teng?\n>>>"))
if javob!=72:
    print("javob xato!")
else:
    print("siz to'g'ri topdingiz")
'''
'''

yosh=int(input("yoshingiz nechada\n>"))
if yosh>= 18:
    print('xush kelibsiz')
else:
    print("sizga kirish mumkin emas")

'''
'''
login=input("yangi login kiriting:\n>")
if len(login)<=5:
    print("login 5 harfdan ko'proq bo'lishi shart")

'''

'''
yil=int(input("tug'ilgan yilingizni kiriting:\n"))
if 2024-yil<18:
    print(f"uzr yoshingiz {2024-yil} da ekan")
    print('kirish mumkin emas')
else:
    print("xush kelibsiz")
'''
'''
yosh = int(input("yoshingiz nechada\n>"))
if yosh>65:print("siz covid-19 xavf guruhida ekansiz")

'''
'''
x,y=25,50
print("x>y") if x>y else print("x<y")
'''

#AMALIYOT
'''

yangi_cars=['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in yangi_cars:
    if car=='gm':
        print(car.upper())
    else:
        print(car.title())


'''
'''
yangi_cars=['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in yangi_cars:
    if car!='gm':
        print(car.title())
    else:
        print(car.upper())

'''
'''

login=input("ismingizni kiriting\n>")
if login.lower()=='admin':
    print("Xush kelibsiz Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login}")

'''

'''
print("Ikkita son kiriting")
son1=int(input('1-sonni kiriting\n>'))
son2=int(input("2-sonni kiriting\n>"))
if son1==son2:
    print("sonlar teng ekan")
else:
    print("sonlar teng emas")
'''
'''
print("istalgan sonni kiriting")
a=int(input("sonni kiriting\n"))
if a>0:
    print("Musbat son")
else:
    print("manfiy son")
'''

a=int(input("istalgan sonni kiriting\n"))
if a>0:
    print(a**(1/2))
else:
    print("musbat sonni kiriting")









