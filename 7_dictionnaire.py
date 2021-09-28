
#coding:utf-8

"""
    + dictionnaire <=> tableau associatif 
        - association clé:valeur
    + creation dictionnaire 
        - dic = {} # vide
        - dic = {<cle>:<valeur>, <cle>:<valeur>}
    + accès à une valeur
        - dic[<clé>]
    + ajout e modification au dictionnaire 
        - dic[<clé>] = <valeur>
    + suppression au dictionnaire 
        - dic.pop(<clé>)
        - del dic[<clé>]
    + vérifier si un élément existe dans le dictionnaire
        - on check l'existance d'une clé
    + parcourir le dictionnaire
        - for key in dictionnaire.keys()
        - for value in dictionnaire.values()
        - for k,v in dictionnaire.items():
    + copie dictionnaire
        - dic2 = dic.copy()
    + passer parametres només dans une fonction
        - **parametres nommé => p=125, test="ok"
"""

# creation dictionnaire 
dictionnaire = {1:145, "prénom":"Omar"}

# accès à une valeur
print(dictionnaire[1])
print(dictionnaire["prénom"])

# ajout e modification au dictionnaire 
dictionnaire["chien"] = "c'est une amis de l'homme" 
print(dictionnaire)

# suppression au dictionnaire 
#dictionnaire.pop("chien")
del dictionnaire["chien"]
print(dictionnaire)

# vérifier si un élément existe dans le dictionnaire
if "prénom" in dictionnaire:
    print("trouvé")
else:
    print("non trouvé")

# parcourir le dictionnaire
for key in dictionnaire.keys():
    print(key)

for value in dictionnaire.values():
    print(value)

for (k,v) in dictionnaire.items():
    print("clé : {} -> valeur : {}".format(k, v))

# copie dictionnaire
dic2 = dictionnaire.copy()
print(dictionnaire)
print(dic2)
dic2["ok"] = "ok"
print(dictionnaire)
print(dic2)

# passer parametres només dans une fonction
def trouverParametres(**parametres):
    print(parametres)

trouverParametres(p=125, test="ok")
