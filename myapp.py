print('-------------------------ÚROKOVÁ KALKULAČKA-------------------------')

vyse_vkladu = input('Zadejte výši vkladu:')
while not (vyse_vkladu.isnumeric() and int(vyse_vkladu)>0):
    print('Výše vkladu musí být kladné číslo')
    vyse_vkladu = input('Zadejte výši vkladu:')

vyse_uroku = input('Zadejte výši úrokové sazby (v %):')
while not (vyse_uroku.isnumeric() and int(vyse_uroku)>0):
    print('Výše úroku musí být kladné číslo')
    vyse_uroku = input('Zadejte výši úrokové sazby (v %):')

delka_sporeni = input('Zadejte délku spoření (počet let):')
while not (delka_sporeni.isnumeric() and int(delka_sporeni)>0):
    print('Délka spoření musí být kladné číslo')
    delka_sporeni = input('Zadejte délku spoření (počet let):')

vyse_uroku=int(vyse_uroku)
vyse_vkladu=int(vyse_vkladu)
delka_sporeni=int(delka_sporeni)

vlozena_castka = float(vyse_vkladu)

print('--------------------------------------------------------------------')

for x in range(delka_sporeni):
    vyse_vkladu=vyse_vkladu + vyse_vkladu*float(vyse_uroku / 100)
    print('Částka na účtu v {}. roce spoření činí: {} Kč'.format(x+1, vyse_vkladu))

print('-----------------------------SUMARIZACE-----------------------------')
uroky=float(vyse_vkladu)-float(vlozena_castka)
print('Vložená částka: {} Kč'.format(vlozena_castka))
print('Úroky: {} Kč'.format(uroky))
print('Daň z úroků: {} Kč'.format((uroky*0.15)))
print('Po odečtení daně bude v {}. roce spoření na daném účtu: {} Kč'.format((delka_sporeni),(vyse_vkladu-(uroky*0.15))))
print('--------------------------------------------------------------------')

# # promenne
# vysledek = 0
# pocetOtazek = 10
# spravne = 'Správná odpověď. Získáváš jeden bod!'
# spatne = 'Špatná odpověď. Zkus další otázku.'
#
# print("-------------ZNALOSTNÍ TEST PYTHON-------------")
#
# otazka1 = input('Je Python vysokoúrovňový jazyk? (y/n)')
# if (otazka1 == "y"):
#     print(spravne)
#     vysledek += 1
# else:
#     print(spatne)
#
# otazka2 = input('Python navrhl Guido van Rossum (y/n)')
# if (otazka2 == "y"):
#     print(spravne)
#     vysledek += 1
# else:
#     print(spatne)
#
# otazka3 = input('Python není dynamicky interpretovaný jazyk (y/n)')
# if (otazka3 == "n"):
#     print(spravne)
#     vysledek += 1
# else:
#     print(spatne)
#
# otazka4 = input('Python je inspirován programovacím jazykem ABCD (y/n)')
# if (otazka4 == "n"):
#     print(spravne)
#     vysledek += 1
# else:
#     print(spatne)
#
# otazka5 = input('Python je hybridní jazyk (nebo také multiparadigmatický) (y/n)')
# if (otazka5 == "y"):
#     vysledek += 1
#     print(spravne)
# else:
#     print(spatne)
#
# otazka6= input('Nebezpečnou vlastností Pythonu je, že obsahuje dokumentované funkce a lokální proměnné (y/n)')
# if (otazka6 == "n"):
#     print(spravne)
#     vysledek += 1
# else:
#     print(spatne)
#
# otazka7= input('Pro Python je v provozu jeho vlastní repozitář balíčků s knihovnami, PyPI, který podporuje snadnou instalaci balíčků programem pip. (y/n)')
# if (otazka7 == "y"):
#     print(spravne)
#     vysledek += 1
# else:
#     print(spatne)
#
# otazka8= input('Jython je implementace Pythonu pro prostředí JMV. Je implementován v jazyce Java. (y/n)')
# if (otazka8 == "n"):
#     print(spravne)
#     vysledek += 1
# else:
#     print(spatne)
#
# otazka9= input('K význačným vlastnostem jazyka Python patří jeho jednoduchost z hlediska učení. (y/n)')
# if (otazka9 == "y"):
#     print(spravne)
#     vysledek += 1
# else:
#     print(spatne)
#
# otazka10= input('Programování v Pythonu klade velký důraz na produktivitu práce programátora. Myšlenky návrhu jazyka jsou shrnuty ve filosofii Pythonu. (y/n)')
# if (otazka10 == "y"):
#     print(spravne)
#     vysledek += 1
# else:
#     print(spatne)
#
# print('Tvé skóre: {}'.format(vysledek))