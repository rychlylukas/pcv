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