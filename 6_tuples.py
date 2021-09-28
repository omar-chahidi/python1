#coding:utf-8

"""
    + /!\ Tuple : conteneur immuable (dont on ne peut pas modifier les valeurs)
    + est un conteneur (key, value)
    + on ne peut pas modifier / ajouter / supprimer un element dans tuple
    + création de tuples :
        - monTuple = ()         # vide
        - monTuple = 17,        # une seule valeur
        - monTuple = (17,)      # une seule valeur
        - monTuple = (17, 2)    # plusieurs valeurs
    + Accès aux valeurs :
        - monTuple = [X]        # valeur d'indice X
    + deux raisons d'utiliser les tuples: 
        - affectation multiple des valeurs à des variables
        - return multiple de valeurs dans une fonction
"""

# /0/ création un tuple
monTuple = (45, 64)
print(monTuple[0])

# /1/ affectation multiple des valeurs à des variables . Je peux modifier les variables
nombre1 , nombre2 = 6 , 3
print(nombre1)
print(nombre2)

# /2/ return deux valeurs dans une fonction
def getPlayerPosition():
    posX = 148
    posY = 86
    return(posX, posY)

#programme principal
coordX = 0
coordY = 0
print("Position du joueur : ({} / {})".format(coordX, coordY))
(coordX, coordY) = getPlayerPosition()
print("Position du joueur : ({} / {})".format(coordX, coordY))
