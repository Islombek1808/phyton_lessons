# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 10:55:27 2024

@author: iBro_SERVICE
"""
'''
cars=['Lacetti', 'nexia', 'malibu', 'cobalt', 'epica', 'tracker', 'captiva']
cars[0].lower()
print(cars)
'''
#fruits=['olma', "o'rik", 'Behi','anor','uzum', 'bodom','nok']

'''fruits.sort()
fruits[0]=fruits[0].lower()
fruits.sort()
fruits.sort(reverse=True)
print(fruits)
'''
'''
print(sorted(fruits, reverse=True))
fruits.reverse()
print("Bizda",len(fruits),"dona meva bor.")
'''

'''
sonlar=list(range(1,21))

juft_sonlar=list(range(2,21,2))
toq_sonlar=list(range(1,21,2))
butun_sonlar=list(range(-2,21))
'''
#min max sum
'''
narxlar=[24388, 53632, 25242, 53462, 76543, 63542]
arzon=min(narxlar)
qimmat=max(narxlar)
jami=sum(narxlar)
'''
'''
butun_sonlar=list(range(-5,10)) # ro'yxat yaratish
natural_sonlar=butun_sonlar[6:]# kesib olish
manfiy_sonlar=butun_sonlar[:5]
butun_sonlar2=butun_sonlar[:]# nusxa ko'chirishda
# shu usuldan foydalanish kerak

'''
'''
oyoq_kiyimlar=('krosovka', 'etik', 'tufli', 'shippak', 'tapochka', 'kavush')
oyoq_kiyimlar=list(oyoq_kiyimlar)
oyoq_kiyimlar.append('sapok')
oyoq_kiyimlar=tuple(oyoq_kiyimlar)
print(oyoq_kiyimlar[-1])
'''


#### AMALIYOT
'''
davlatlar=['uzbekistan', 'tadjikistan', 'russian', 'turkmenistan', 'krygzstan',
'pakistan', 'india', 'turkey', 'usa', 'kitay', 'korea', 'japan']
print(davlatlar)
print(len(davlatlar))

#print(sorted(davlatlar, reverse=True))

#davlatlar.reverse()

davlatlar.sort()
davlatlar.reverse()
'''
'''

juft_sonlar=list(range(120,1200,2))

yigindi=sum(juft_sonlar)
ayirma=max(juft_sonlar)-min(juft_sonlar)
uzunlik=len(juft_sonlar)
print(juft_sonlar[:20])
print(juft_sonlar[260:280])
print(juft_sonlar[-20:])
'''
#taomlar

taomlar=['kulchatoy', 'osh', 'manti', 'xonim', 'somsa', "go'ja"]
nonushta=taomlar[:]
nonushta.remove('kulchatoy')
del nonushta[0]
del nonushta[1]
nonushta.append('sumalak')
nonushta.append('xalisa')
print(nonushta,"\n",taomlar)

nonushta=tuple(nonushta)
nonushta=list(nonushta)

#nonushta[0]='qaymoq va non'









