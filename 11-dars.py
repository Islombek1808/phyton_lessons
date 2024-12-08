# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 22:09:56 2024

@author: iBro_SERVICE
"""
"""
#if-elif-else operatori
yosh=int(input("yoshingizni kiriting\n>"))
if yosh<=4:
    narx=3000
elif yosh<=12:
    narx=5000
elif yosh<=18:
    narx=8000
else:
    narx=10000
print(f"Sizga kirish {narx} so'm")
    """
    ###DAM OLISH KUNI
'''
kun=input("Bugun kun qaysi kun?\n>")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('bugun dam olish kuni')
else:
    print("bugun ish kuni")
'''
'''
kun=input("bugun kun qaysi?\n>")
harorat=float(input("havo harorati necha gradus?\n>"))
if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
    print("cho'milgani ketdik")
elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
    print("uyda dam olamiz")
else:
    print("ishga bor axmoq")

'''

"""
### BOOLEAN
narx=20000
choy=True
salat=False

if choy and salat:
    narx=narx+10000
elif choy or salat:
    narx=narx+5000
print(f" jami summa {narx} so'm")

"""




'''
### BOOLEAN
narx=20000
choy=True
salat=1
non=True
kompot=True
shirinlik=1
if choy:
    print("Mijoz choy oldi")
    narx=narx+3000
if salat :
    print("Mijoz salat oldi")
    narx=narx+4000
if non:
    print("Mijoz non oldi")
    narx=narx+3500
if kompot:
    print("Mijoz kompot oldi")
    narx=narx+6000
if shirinlik:
    print("Mijoz shirinlik oldi")
    narx=narx+8000
print(f"jami narx {narx} so'm")

'''
# RO'YXAT TARKIBINI TEKSHIRISH IN OPERATORI
'''
menu=['osh', 'kabob', 'xonim', 'chuchvara', 'somsa', 'xalisa']
if 'manti' in menu:
    print("1")
else:
    print("0")
'''

"""
menu=['osh', 'manti', 'somsa', 'xonim', 'chuchvara', 'kabob', 'shirguruch']
buyurtma=input("Janob nima ovqat yeysiz?\n>")
if buyurtma.lower() in menu:
    print("buyurtmangiz qabul qilindi")
else:print("Uzr, afsuski bizda bunday taom yo'q")
'"""
'''
menu=['osh', 'manti', 'somsa', 'xonim', 'chuchvara', 'kabob', 'shirguruch']
buyurtma=input("Janob nima ovqat yeysiz?\n>")
if buyurtma.lower() not in menu:
    print("buyurtmangiz qabul qilinmadi")
    print("0")
else:
    print("buyurtma qabul qilindi") 
    print("1")
'''
"""
menu=['osh', 'manti', 'somsa', 'xonim', 'chuchvara', 'kabob', 'shirguruch']
buyurtmalar=['manti', 'chuchvara', 'shashlik', 'kabob', 'xalisa']
for taom in buyurtmalar:
    if taom in menu:
        print(f"{taom} menyuda bor,buyurtma qabul qilindi")
    else:
        print(f"afsuski bizda {taom} yo'q")

"""

"""
menu=['osh', 'manti', 'somsa', 'xonim', 'chuchvara', 'kabob', 'shirguruch']
buyurtmalar=['manti', 'chuchvara', 'shashlik', 'kabob', 'xalisa']
if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f"menuda {taom} bor")
        else:
            print(f"menuda {taom} yo'q")
else:
    print("buyurtma berilmagan")
"""
####AMALIYOT   AMALIYOT AMALIYOT


'''
juft_son=int(input("juft son kiriting\n>"))
if juft_son%2==0:
    print("rahmat")
else:
    print("BU juft son emas")
'''
'''
yosh=int(input("yoshingizni kiriting\n>"))
if (yosh<4 or yosh>60):
    print('sizga kirish tekin')
elif (yosh>4 and yosh<18):
    print("sizga kirish 10000")
elif yosh>=18 and yosh<=60:
    print("sizga kirish 20000 so'm")


'''

'''
a=int(input('a sonini kiriting\n>'))
b=int(input('b sonini kiriting\n>'))
if a>b:
    print("a>b")
elif a<b:
    print("a<b")
else:
    print("a=b")
'''
"""
mahsulotlar=['makaron', 'un', 'olma', 'shakar', 'yog\'', 'pomidor', 
             'bodring', 'sabzi', 'piyoz', 'mayiz', 'bodom' ]
savat=[]
soni= int(input(" Nechta mahsulot olasiz\n>>>"))
for mahsulot in range(soni):
    savat.append(input(f"{mahsulot+1}-mahsulotni kiriting\n>>>"))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"{mahsulot} do'konimizda bor")
    else:
        print(f"{mahsulot} do'konimizda yo'q")

"""
"""
mahsulotlar=['makaron', 'un', 'olma', 'shakar', 'yog\'', 'pomidor', 
             'bodring', 'sabzi', 'piyoz', 'mayiz', 'bodom' ]
bor=[]
yoq=[]
soni= int(input(" Nechta mahsulot olasiz\n>>>"))
for mahsulot in range(soni):
    mol=(input(f"{mahsulot+1}-mahsulotni kiriting\n>>>"))
    if mol in mahsulotlar:
        bor.append(mol)
    else:
        yoq.append(mol)
        
if not yoq:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
else:
    print(f"quyidagi mahsulotlar do'konimizda bor: {bor}")
    print(f"quyidagi mahsulotlar do'konimizda yoq: {yoq}")
        
   """

'''
foydalanuvchilar=['islom', 'anvar', 'oybek', 'nodir', 
                  'rustam', 'botir', 'davron']     
yangi=input('yangi login  kiriting\n>>>')
if yangi.lower() in foydalanuvchilar:
    print('Bu login band, iltimos boshqa login kiriting')
    yangi=input('yangi login  kiriting\n>>>')
else:
    print(f"Xush kelibsiz, {yangi.title()}")

'''

a=int(input('butun son kiriting'))
b=[]
for son in range(2,11):
    if a%(son)==0:
        b.append(son)
print(f"{a} soni {b} sonlariga qoldiqsiz bo'linadi")




























