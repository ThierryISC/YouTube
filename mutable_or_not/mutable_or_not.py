
def ajoute_au_panier(artcile, chariot=None):
    if chariot is None:
        chariot=[]
    chariot.append(artcile)
    return chariot

print('1: ', ajoute_au_panier("Chaussures"))
print('2: ', ajoute_au_panier("T-Shirt"))