# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 19:53:35 2024

@author: iBro_SERVICE
"""

#AMALIYOT AMALIYOT AMALIYOT AMALIYOT
'''
son = float(input("Juft son kiriting: "))
if son%2==0:
    print("Rahmat!")
else:
    print("Bu son juft emas.'")
    '''
'''   
yosh = int(input("Yoshingiz nechida?"))

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
    
print(f"Chipta {narh} so'm")
'''
'''
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")
    '''
    
'''
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

savat=[]

for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
       
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
m=0
for mahsulot in savat:
     if mahsulot=='':
         m=m+1
if m==5: 
    print("Savatingiz bo'sh")            
'''

'''
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print("Do'konimizda quyidagi mahsulotlar yo'q:")
for mahsulot in mavjud_emas:
  print(mahsulot)
if not len(mavjud_emas):
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
 '''




users = ['alisher1983','aziza','yasina' 'umar']

login = input("Yangi login tanlang:" )

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")       
    
    
    