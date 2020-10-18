'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81373 #? normální pozemské tíhové zrychlení v Praze
MOON_GRAVITY = 1.62 #? měsíční gravitace
MOON_TO_EARTH = 384400000 #vzdálenost Země k Měsíci
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND =  343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu



def volny_pad():
    '''
    Výpočet rychlosti volného pádu
    '''
    print('Výpočet rychlostí volného pádu na Zemi a Měsíci')
    t = input('Zadejte čas v sekundách: ')
    rychlost = int(t) * EARTH_GRAVITY
    print('Rychlost volného pádu na Zemi je: {} m/s'.format(rychlost))
    rychlost = int(t) * MOON_GRAVITY
    print('Rychlost volného pádu na Měsíci je: {} m/s'.format(rychlost))

print('\n')

def paprsek():
    '''
    Za jak dlouho urazí světelný paprsek vzdálenost Země - Měsíc?
    '''
    print('Za jak dlouho urazí světelný paprsek vzdálenost Země - Měsíc?')
    print('Počítáme s rychlostí světla o velikosti: {} m/s'.format(SPEED_OF_LIGHT))
    print('Počítáme se vzdáleností Země od Měsíce: {} m'.format(MOON_TO_EARTH))
    print('Paprsek urazí tuto vzdálenost za {} sekundy'.format(MOON_TO_EARTH/SPEED_OF_LIGHT))

print('\n')

def skala():
    '''
    Jak daleko je skála, od které se ozvěnou vrátil zvuk za 1,5s?
    '''
    print('Jak daleko je skála, od které se ozvěnou vrátil zvuk za 1,5s?')
    t = 1.5
    print('Počítáme s časem o velikosti: {} s'.format(t))
    print('Počítáme s rychlostí zvuku ve vzduchu o velikosti: {} m/s'.format(SPEED_OF_SOUND))
    print('Skála je vzdálena {} metr(ů)'.format(SPEED_OF_SOUND*t/2))


''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''