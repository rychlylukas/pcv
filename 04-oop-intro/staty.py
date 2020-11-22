class Staty:
    def __init__(self, nazev, pocet_obyvatel, rozloha):
        self.nazev = nazev
        self.pocet_obyvatel = pocet_obyvatel
        self.rozloha = rozloha

class CovidStaty(Staty):

    clenstvi = ['OSN']
    pocet_statu = 0

    def __init__(self, nazev, pocet_obyvatel, pocet_nakazenych, rozloha):
        super().__init__(nazev, pocet_obyvatel, rozloha)
        self.pocet_nakazenych = pocet_nakazenych
        CovidStaty.pocet_statu += 1

    def promorenost(self):
        return round((float(self.pocet_nakazenych/self.pocet_obyvatel)*100),3)

    def nakazeni_rozloha(self):
        return round(float(self.pocet_nakazenych/self.rozloha), 2)

    def vypis_promorenost(self):
        return '{} má {} obyvatel, promořenost koronavirem v této zemi činí: {}%'.format(self.nazev, self.pocet_obyvatel, self.promorenost())

    @classmethod
    def evropske_staty(cls, organizace):
        cls.clenstvi.append(organizace)

    @staticmethod
    def narust(nakazeni, r):
        return nakazeni * r

    def __str__(self):
        return '{} má {} obyvatel, aktuálně je v zemi nakaženo koronavirem: {} lidí.'.format(self.nazev, self.pocet_obyvatel, self.pocet_nakazenych)
    def __gt__(self, other):
        return self.promorenost() > other.promorenost()
    def __lt__(self, other):
        return self.promorenost() < other.promorenost()
    def __eq__(self, other):
        return self.promorenost() == other.promorenost()
    def __mul__(self, r):
        return self.pocet_nakazenych * r
    def __add__(self, other):
        return self.pocet_nakazenych + other.pocet_nakazenych

stat1 = CovidStaty('Česká republika', 10690000, 88825, 78866)
stat2 = CovidStaty('Německo', 83020000, 305407, 357023)
r = 1.1
nakazeni = 1000

print('\n')
print('Pokud je dnes {} nakažených, zítřejší přírustek při reprodukčním čísle r = {} bude činit {} nakažených.'.format(nakazeni, r, CovidStaty.narust(nakazeni, r)))
print('\n')
print('Počet zapsaných států: {}'.format(CovidStaty.pocet_statu))
print('\n')
print(stat1.vypis_promorenost())
CovidStaty.evropske_staty('EU')
print('\n')
print(stat1)
print('\n')
if(stat1>stat2):
    print('{} má vyšší promořenost než {}.'.format(stat1.nazev, stat2.nazev))
else:
    print('{} má vyšší promořenost než {}.'.format(stat2.nazev, stat1.nazev))
if(stat1<stat2):
    print('{} má nižší promořenost než {}.'.format(stat1.nazev, stat2.nazev))
else:
    print('{} má nižší promořenost než {}.'.format(stat2.nazev, stat1.nazev))
if(stat1==stat2):
    print('{} má stejnou promořenost jako {}.'.format(stat1.nazev, stat2.nazev))
else:
    print('{} nemá stejnou promořenost jako {}.'.format(stat2.nazev, stat1.nazev))
print('\n')
print('Pokud má dnes {} {} nakažených, zítra bude při reprodukčním čísle {} {} nakažených'.format(stat1.nazev, stat1.pocet_nakazenych, r, round(stat1 * r)))
print('{} a {} má dohromady {} aktuálně nakažených.'.format(stat1.nazev, stat2.nazev, stat1 + stat2))

class UdajeStaty(Staty):

    def __init__(self, nazev, pocet_obyvatel, rozloha, prezident, premier, hlavni_mesto):
        super().__init__(nazev, pocet_obyvatel, rozloha)
        self.prezident = prezident
        self.premier = premier
        self.hlavni_mesto = hlavni_mesto

    def __str__(self):
        return '{} s hlavním městem {} a rozlouhou {} km2 má {} obyvatel. V čele státu stojí prezident/ka {} a premiér/ka {}.'.format(self.nazev, self.hlavni_mesto, self.rozloha, self.pocet_obyvatel, self.prezident, self.premier)

stat1 = UdajeStaty('Česká republika', 10690000, 78866, 'Miloš Zeman', 'Andrej Babiš', 'Praha')
print('\n')
print(stat1)
