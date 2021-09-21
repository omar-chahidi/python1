# fonction input 
#-----------------------------------------------------------------
age = input("Quel âge as-tu ? ")
age = int(age)
print("Tu as {} ans".format(age))

# fonction sans paramètre 
#-----------------------------------------------------------------
def direBonjour():
    print("Bonjour tout le monde ! :)")

direBonjour()

# fonction avec paramètre (avec paramète obligatoire ou optionnel)
#-----------------------------------------------------------------
def compteUtilisateur(loginUtilisateur="oci", pwdUtilisateur="123", ageUtilisateur=age):
    print("Login = {} & mot de passe = {} -> l'âge = {}".format(loginUtilisateur, pwdUtilisateur, ageUtilisateur))
compteUtilisateur("Omar", "7777")
compteUtilisateur("Tom")
compteUtilisateur()
compteUtilisateur(loginUtilisateur="e599352", pwdUtilisateur="2021", ageUtilisateur=40)

# fonction avec une liste de paramète 
#-----------------------------------------------------------------
def showInventory(*list_items):
    for item in list_items:
        print(item)

showInventory("épée")
showInventory("épée", "arc", "potion de mana", "cape de Dragon rouge")


# fonction qui calcul la somme de deux nombres et renvoie le résultat 
#-----------------------------------------------------------------
def trouverNombreLePlusGrand(nombr1, nombre2):
    if nombr1 > nombre2:
        return nombr1
    elif nombr1 < nombre2:
        return nombre2
    else:
        return "nombr1 = nombr2"

print(trouverNombreLePlusGrand(5, 5))

"""
 Fonction anonyme "lambda"
    Si on a une seule instruction on ne va pas créer une fonction mais 
    on va faire une fonction anonyme 
"""
# fonction anonyme <=> qui n'a pas de nom
#-----------------------------------------------------------------
coucou = lambda:print("Bonjousr")
coucou()

# fonction anonyme avec une seule instruction => calcul prix TTC
#-----------------------------------------------------------------
prixTTC = lambda prixHT: prixHT + (prixHT*20/100)
print(prixTTC(24))

# fonction anonyme calculer la somme de deux nombres
#-----------------------------------------------------------------
calculerLasommeDeDeuxNombres = lambda a, b : a + b
print(calculerLasommeDeDeuxNombres(24, 1))