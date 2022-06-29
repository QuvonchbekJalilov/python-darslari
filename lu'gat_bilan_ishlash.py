

# telefon = {'model':'iphone 13 pro max',
#            'rang':"qora",
#            'xotirasi':'128 GB',
#            'narxi':'1400$'}
# print(f"{telefon['model']} ,rangi {telefon['rang']}, xotirasi {telefon['xotirasi']},narxi esa {telefon['narxi']}")

# talaba = {'ism':'Jalilov Quvonhcbek',
#         'yosh':19,
#         "oqish_joyi": "MDIST",
#         'fakultet': 1,
#         'sohasi': "BACKEND DEVELOPER"}
# print(f"Mening ismim {talaba['ism'].upper()}, \
#     yoshim {talaba['yosh']}da , \
#     men {talaba['oqish_joyi']}da {talaba['fakultet']} kursda o'qiyman ,\
#     mening soham {talaba['sohasi'].lower()}")


# dadam = {'ism':'Syunov Mansur ',
#         'yoshi':42,
#         'tugulgan_joyi':'Qashqadaryo',
#         'malumoti':'oliy',
#         'kasbi': 'tadbirkor'}
# oyim = {'ism':'Jumayeva Dilafruz',
#         'yoshi':38,
#         'malumot':"o'rta",
#         'kasbi':'uy bekasi'}
# singlim = {'ism':'Jalilova Visola',
#         'yoshi':16,
#         'malumot':"o'rta",
#         'kasbi':"o'quvchi"}
# print(f"Otamning ismi {dadam['ism']}, {2022-dadam['yoshi']} yilda, {dadam['tugulgan_joyi']} viloyatida tug'ulgan.")


# sevimli_taom ={'dadam':'osh,manti',
#                 'oyim':"sho'rva",
#                 'singlim':'shashlik,lavash',
#                 'men':'osh,lavash'}
# print(f"""Dadamning sevimli taomlari {sevimli_taom['dadam']},
# oyimniki esa {sevimli_taom['oyim']},
# va mening sevimli taomim {sevimli_taom['men']} """)




# lugatlar = {'apple':'olma',
#         'banana':'banan',
#         'watermelon':'tarvuz',
#         'strawberry':'qulupnay'}
# soz_kirit =[]
# soz_kirit.append(input("so'z kiriting,tarjima qilamiz: "))


# for lugat in soz_kirit:
#         if lugat in lugatlar:
#          print(f"{lugat} tarjimasi {lugatlar['watermelon']} ")
#         elif lugat in lugatlar :
#          print(f"{lugat} tarjimasi {lugatlar['banana']} ")
#         elif lugat in lugatlar:
#          print(f"{lugat} tarjimasi {lugatlar['apple']} ")
#         elif lugat in lugatlar:
#          print(f"{lugat} tarjimasi {lugatlar['strawberry']} ")

#         else:
#          print(f"bunday so'z mavjud emas")



# lugatlar = {'apple':'olma',
#         'banana':'banan',
#         'watermelon':'tarvuz',
#         'strawberry':'qulupnay'}

# lugatlar['pineapple'] = 'shaftoli'
# lugatlar['ananas']= 'ananas'

# print(lugatlar)

# ismlar ={}
# ismlar['ism']='jalilov quvonchbek'
# ismlar['yoshi']= 19
# ismlar['t_joy']= 'qashqadaryo'
# print(ismlar)



# talaba = {'ism':'Jalilov Quvonhcbek',
#         'yosh':19,
#         "oqish_joyi": "MDIST",
#         'fakultet': 1,
#         'sohasi': "BACKEND DEVELOPER"}

# talaba['ism']='Qobilov Sanjar'

# del talaba['ism']
# print(talaba)

# talaba={}
# talaba['ism'] = 'Malika'
# talaba['yosh'] = '18'
# talaba['t_joyi'] = 'toshkent shahri'
# del talaba['ism']

# print(talaba)

# bitirgan_oquvchilar = {'ism':'shahzod',
#                 'ism':'anvar',
#                 'ism':'farangiz',
#                 'ism':'malika',
#                 'ism':'dilnoz'}
# print(bitirgan_oquvchilar)

#get metodi haqida

# telefonlar = {'dilshod':'iphone 13 pro max',
#                 'sherzod':'redmi',
#                 'samandar': 'vivo',
#                 'Quvonchbek':'redmi note 8 pro'}

# telefon = telefonlar.get('Muhammad',"bunday shaxs mavjud emas.")
# print(f" sherzodning telefoni {telefonlar['sherzod']}, samandarning telefoni esa {telefonlar['samandar']}, {telefon}")
# print(telefon)


# items() metodi haqida


# dasturchi = {'ism':'Quvonchbek',
#         'familiya': 'Jalilov',
#         'yosh': 19,
#         'fakultet': 'backend',
#         'kurs': 1}

# for kalit,qiymat in dasturchi.items():
#       print(f"kalit soz : {kalit}")  
#       print(f"qiymati: {qiymat} \n")

# print(dasturchi.items())



# moshina = {'quvonchbek':'bugatti',
#         'sherali':'kia',
#         'samandar':'tayotta',
#         'muhammad':'lombargini',
#         'dilshod':'gentra'}

# for kalit,qiymat in moshina.items():
#         print(f"{kalit.title()}ning moshinasi, {qiymat.upper()} \n")



# 1- uyga vazifa


# from multiprocessing import Value


en_uz ={ 'big':'katta',
        'huge':'ulkan',
        'community':'jamoa',
        'altarnative':'muqobil',
        'experience':'tajriba',
        'climate':'iqlim',
        'wage':'haftalik oylik',
        'sensitive':'nozik',
        'handsome':'kelishgan',
        'teenager':"o'smir",
        'child':'bola',
        'database':"ma'lumotlar bazasi"}
for kalit,qiymat in sorted(en_uz.items()):
        print(f"{kalit.title()} so'zining tarjimasi {qiymat}")

# 2 - uyga vazifa

# t_shaxslar = {'Amir Temur': 1336,
#                 'Alisher Navoiy': 1441,
#                 "Mirzo Ulug'bek" : 1394,
#                 'Ozod Sharafiddinov': 1929}
# for kalit,qiymat in sorted(t_shaxslar.items()):
#         print(f"{kalit} {qiymat} yilda tug'ulgan.")


# 3 - uyga vazifa 

# from multiprocessing import Value



# davlat_poytaxt = {'amerika':'washington',
#                 'fransiya':'paris',
#                 'angliya':'london',
#                 'portugaliya':'lissabon',
#                 'kanada':'ottava',
#                 'ukraina':'kiyev',
#                 'italiya': 'rim',
#                 'birlashgan arab amirliklari':'abu dabi',
#                 'germaniya':'berlin',
#                 "o'zbekiston":'toshkent'}

# davlat = input("davlat kiriting, poytaxtini chiqarib beramiz: ")

# capital = davlat_poytaxt.get(davlat)
# if capital == None:
#         print("Kechirasiz, bizda bu haqida ma'lumot yo'q")
# else:
#         print(f"{davlat.upper()}ning poytaxti {capital.title()} shahri")

# 4 - uyga vazifa

fast_foods = {'lavash': 22000,
              'xot-dog': 15000,
              'tandir lavash':24000,
              'burger': 21000,
              'cheese burger':17000,
              'longer':18000}

buyurtma = []
for n in range(4):
        buyurtma.append(input(f"{n+1} - buyurtmangiz nima?  "))

for mijoz in buyurtma:
        if mijoz in fast_foods:
                print(f"{mijoz.title()} bor, narxi {fast_foods[mijoz]}- so'm.")
        else:
                print(f"{mijoz} yo'q edi.")


# dostlar = {'sherali':'redmi',
#         'dilshod':'vivo',
#         'samandar':'iphone',
#         'doston':'realme',
#         'xurshid':'iphone',
#         'ilyos':'redmi'}

# print("mening dostlarim quyidagi telefon modellarini ishlatishadi ")
# for dost in set(dostlar.values()):
#         print(dost.title())



# dostlar = {'sherali':'redmi',
#         'dilshod':'vivo',
#         'samandar':'iphone',
#         'doston':'realme',
#         'xurshid':'iphone',
#         'ilyos':'redmi'}
# print("")
# for dost in sorted(dostlar):
#         print(dost.title())