def sort_vyskyt(prvek_set):
    return prvek_set[1]

def charFrequency(veta):
    pole = [(znak, veta.count(znak)) for znak in set(veta)]
    return sorted(pole, key=sort_vyskyt, reverse=True)


print(charFrequency("Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."))

# def charFrequency(veta):
#     seznam_znaku={}
#     for i in veta:
#         if i in seznam_znaku:
#             seznam_znaku[i] += 1
#         else:
#             seznam_znaku[i] = 1
#     print(seznam_znaku)
#
# charFrequency("Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech.")