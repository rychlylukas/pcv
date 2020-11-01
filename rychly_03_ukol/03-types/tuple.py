'''
Tuples - neměnitelné n-tice hodnot (seřazený seznam prvků)
In Python tuples are written with round brackets.
//V Pythonu jsou tuples psány v kulatých závorkách
'''

# Vytvoření tuples
numbers = (1, 2, 3)
print('numbers: ', numbers)
print('Type(numbers): ',type(numbers))

chars = tuple('Hello world')
print('chars: ', chars)
print('Type(chars): ',type(chars))

# To create a tuple with only one item, you have add a comma after the item, unless Python will not recognize the variable as a tuple.
# //K vytvoření tuple s jednou položkou musíme přidat čárku za danou položku, jinak by Python nepoznal, že se jedná o tuple.
colors = ('red',)
print('colors: ', colors)

# Součet tuples
print(f'chars + numbers: {chars + numbers}')

# Výpis hodnot 
# You can specify a range of indexes by specifying where to start and where to end the range
# //Můžeme určit rozsah indexů, například začátek a konec.
# When specifying a range, the return value will be a new tuple with the specified items.
# //V případě určení rozsahu nám bude vrácena hodnota nový tuplle se specifickými položkami (v daném rozsahu)
print(f'chars[2:5]: {chars[2:5]}')

# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
# //Negativní indexování znamená, že indexace začíná od konce, -1 vrací poslední položku, -2 vrací předposlední položku, atd.
# Specify negative indexes if you want to start the search from the end of the tuple:
# //Zadejte negativní indexy, pokud chcete začít hledat od konce tuple:
# This example returns the items from index -4 (included) to index -1 (excluded)
# //Tento příklad vrací položky z indexu -4 (včetně) po index -1 (bez)
print(f'chars[-4:-1]: {chars[-4:-1]}')

# To determine how many items a tuple has, use the len() method:
# //Pokud chceme zjistit, kolik položek má tuplle, použijeme metodu len():
print(f'len(chars): {len(chars)}')

# Zjištění prvního výskytu a počtu výskytu prvku
if 'l' in chars:
    print(f'chars.index("l"): {chars.index("l")}')
    print(f'chars.count("l"): {chars.count("l")}')

# Záměna hodnot proměnných
x = 10
y = 2
x, y = y, x
print(f'x: {x}, y: {y}')
