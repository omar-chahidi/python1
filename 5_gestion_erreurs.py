#coding:utf-8

"""
L'objectif est de gérer une exception levée
Gérer les exception : try / except (+ else , finally)
Types exceptiosn : 
    ZeroDivisionError
    ValueError
    TypeError
    NameError
    AssertionError
    ...
"""

#-------------------------------------------------------------------------------------
ageUtilisateur = input("Entrez votre âge ? ")

try:
    ageUtilisateur = int(ageUtilisateur)
except:
    print("Votre âge non valide !")
else:
    print("Votre âge est de", ageUtilisateur)
finally:
    print("FIN DU PROGRAMME ....")
    
# Gérer les erreurs d'une division
# il ne faut pas / 0 ou par un text
# remarque : puisque on ne connait pas les exception des erreurs c'est pour cela 
# on lance le programme pour generer des erreur et ensuite ajouter le nom de l'exception
#-------------------------------------------------------------------------------------
nombre1 = 150

nombre2 = input("Entrer un nombre pour diviser ? ")

try:
   nombre2 = int(nombre2) 
   print("Resultats = {}".format(nombre1 / nombre2))
except ZeroDivisionError:
    print("On ne peut pas diviser par zéro ")
except ValueError:
    print("On ne peut pas diviser par un texte ")
else:
    print("La division est terminé ")
finally:
    print("FIN DU PROGRAMME DE LA DIVISION....")


# Exemple attraper une xception avec AssertionError
# assert prixTTC > 25 EUROS => je veux verifier que le prix est > à 25 euros
#
# avec assert J'exige que le prix est > 25 si non je veux elever une AssertionError
#-------------------------------------------------------------------------------------
try:
    prixTTC = input("Quel est le prix TTC ? ")
    prixTTC = int(prixTTC)
    assert prixTTC > 25 # je veut que le prix soit plus grand que 25 euros
except AssertionError:
    print("J'ai attrappé l'exeption. Le prix choisi est < 25 euros. Test ko")
else:
    print("Le prix est > 25 euros. Tout est OK")
    