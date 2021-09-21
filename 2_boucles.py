
"""
    Boucles
        while
        for
    Mots clés
        break -> casse ou sortir de la boucle
        continue -> revient au début de la boucle
"""
# ----------------------------------------------------------------
sentence = "123456"
for letter in sentence:
    print(letter)



# ----------------------------------------------------------------
compteur = 0

while compteur < 3:
    compteur += 1
    print("Test", compteur)

# ----------------------------------------------------------------
jeu_lance = True
print("")

while jeu_lance:
    choixMenuDuTerminal = input(">> ")
    if choixMenuDuTerminal == "again":
        continue
    elif choixMenuDuTerminal == "quit":
        #jeu_lance = False 
        break
    elif choixMenuDuTerminal == "hello":
        print("bonjour")
    else:
        print("Commande non trouvé")

print("Â bientôt ....")