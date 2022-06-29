
# def avto_info(kompaniya,model,rang,karobka,yili,narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rang,
#             'karobka':karobka,
#             'yili':yili,
#             'narhi':narhi}
#     return avto

# avto1 = avto_info('gm','nexia 3','oq','avto','2019')
# avto2 = avto_info('gm','malibu','qora','avto','2022','40000')
# avtolar = [avto1,avto2]
# print('onlayn bozordagi moshinalar:')
# for avto in avtolar:
#     if avto['narhi']:
#         narh = avto['narhi']
#     else:
#         avto['narhi']="noma'lum"
#     print(f"{avto['rang']} {avto['model']}, narhi {avto['narhi']} ")


# def my_func():
#     print("assalomu alekum")

# my_func()


# def my_func(name):
#     """bu funksiyamiz ism qabul qilib, unga salom beradi"""
#     print(f"Assalomu alekum, {name}")

# my_func("Quvonchbek")
# my_func("Samandar")

# print(my_func.__doc__)



# def talaba(ism, yosh , fakultet, kurs):
#     """bu ism va yoshni qabul qilib , uni konsulga chiqaradi"""
#     print(f"Assalomu alekum {ism.upper()},\nyosh: {yosh},\nfakultet: {fakultet},\nkurs: {kurs}")

# talaba("quvonchbek",19,"Accounting and Finance", 2)


#uyga vazifa - 1

# def my_func(birinchi, ikkinchi):
    
#     birinchi = int(input("birinchi sonni kiriting: "))
#     ikkinchi = int(input("ikkinchi sonni kiriting: "))
#     if birinchi>ikkinchi:
#         print(f"{birinchi}") 
#     elif birinchi == ikkinchi:
#         print("siz kiritgan son teng!")
#     else:
#         print(f"{ikkinchi}")
# my_func('birnchi','ikkinchi')


#uyga vazifa - 2

# def information(name,age):
#     name = input("ismingizni kiriting: ")
#     age = int(input("yoshingizni kiriting: ")) 
#     print(f"{name} {2022-age} da tug'ulgan")
# information('name', 'age' )


#uyga vazifa - 3

# def son_kv_kub():
#     while True:
#         son = int(input("son kiriting kvadrati va kubikini hisoblaymiz: "))
#         print(f"{son} ning kvadarati {son**2} ga teng \nkubi esa {son**3} ga teng.")

# son_kv_kub()


# uyga vazifa - 4

# def son_toq_juft():
#     """bu funksiya toq yoki juftligini aniqlaydi"""
#     while True:
#         son = int(input('son kiriting: '))
#         if son%2 == 0:
#             print(f"{son} soni juft son.")
#         else:
#             print(f"{son} soni juft son emas.")
# son_toq_juft()


# uyga vazifa - 5

# def qoldiqsiz_bolish():
#     son = int(input("son kirting: "))
#     for qoldiqli_bolish in range(2,21):
#         if son% qoldiqli_bolish == 0:
#             print(qoldiqli_bolish)

# qoldiqsiz_bolish()


# def talaba(ism,familyasi,yosh):
#     talabalar= {'ism': ism,
#                 'familyasi': familyasi,
#                 'yoshi': yosh}

#     talabalar = f" talabaning ismi {ism} {familyasi} yoshi {yosh} da"
#     return talabalar

# talaba1 = talaba('Quvonchbek','Jalilov',19)
# talaba2 = talaba('dilshod','shodiyev', 20)

# print("darsga kelgan talabalar:")
# print(f"Birinchi talaba: {talaba1}, \n ikkinchi talaba: {talaba2}")


# def kopaytma():
#     sonlar = list(range(1,51))

#     for son in sonlar:
#         print(f"{son*son} ")
# kopaytma()


# son = list(range(1,30))
# ason = list(range(31,41))

# kv =list(map(lambda x ,y : x * y,son , ason))
# print(kv)


# def moshinalar(nomi,rangi,**qolgan_malumotlar):
#     qolgan_malumotlar['nomi'] = nomi
#     qolgan_malumotlar['rangi'] = rangi

#     return  qolgan_malumotlar

# moshina1 = moshinalar("KIA","qora",narx=50000,yili=2022)
# moshina2 = moshinalar("Malibu",'oq',narx=30000,yil=2022)

# print(moshina1)
# print(moshina2)


# def ismlar(*ism):
#     return ism

# ism1 = ismlar(f"nomi : malibu, rangi : qora, narxi : 30000")

# print(ism1)




# def dasturchi(ism, **dev):
#     dev['ism'] = ism
#     return dev

# moshina1 = dasturchi(ism='olimjon',fam = "berdiyev", yoshi = 24, sohasi='backend')

# print(moshina1)


# from math import sqrt

# number = list(range(11))
# ildiz = list(map(sqrt, number))
# print(ildiz)


