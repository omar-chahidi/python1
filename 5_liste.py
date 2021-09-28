#coding:utf-8

# /1/ Création d'une liste
# inventaire = list() 
# inventaire = [0] *10 #inventaire = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#print(inventaire)

# /2/ parcour les éléments d'une liste puis affichage chaque élément de la liste
inventaire = range(20)
for value in inventaire:
    print(value)

# /3/ affichage la totalité de tous les éléments d'une liste
liste1 = ["item1", "item2", "item3", "item4", "item5", "item6"]
print("affichage la totalité d'une liste =>"               , liste1[:])
print("afficher l'élément d'indice 1 =>"                   , liste1[1]) 
print("afficher les deux premiers éléments de la liste =>" , liste1[:2]) 
print("afficher les trois derniers éléments de la liste =>" ,liste1[3:]) 
print("afficher à partir de l'éléement d'indice 2 à élément d'indice 5-1 =>" ,liste1[2:5]) 

# /4/ modification d'une liste 
liste2 = ["ele1", "ele2", "ele3", "ele4", "ele5"]
liste2[2] = "nouveau élément"
print(liste2[:])
liste2[:] = ["toto"] * len(liste2)
print(liste2[:])

# /5/ recherche un élélement d'une liset
if "ele3" in liste2:
    print("élément ele3 est trouvé")
else:
    print("élément ele3 est non trouvé")

# /6/ utilisation des méthodes : 
    # ajout => append 
    # insertion dans un indice => insert 
    # suppression d'un élé à partir d'un indice => del
    # afficher l'indice d'un élément de ma liste => index  
    # trier une liste => sort
    # inverser les éléments d'une  liste => reverse
    # compter le nombre de fois d'un élément (nombre d'occurence) => count 
    # effacer toutes les éléments d'une liste => clear
    # mettre une chaine de caractère dans une liste => split avec des éspaces
    # mettre une liste en une chaine => joint 
    
liste3 = []
print(liste3[:])
liste3.append("ajout élément 1")
liste3.append("ajout élément 2")
liste3.append("ajout élément 3")
print(liste3[:])
liste3.insert(1, "insersion d'un élément")
print(liste3[:])
#del liste3[1]
print(liste3[:])
print("Indice :", liste3.index("ajout élément 3") )
element_a_supprimer = liste3.index("ajout élément 1")
del liste3[element_a_supprimer]
print(liste3[:])
liste3.remove("insersion d'un élément")
print(liste3[:])

# trier une liset 
liste4 = ["omar", "christophe", "brigitte", "cyril", "brigitte", "michel", "brigitte"]
liste4.sort()
print(liste4[:])
liste4.reverse()
print(liste4[:])
print("nombre d'occurence du brigitte ", liste4.count("brigitte"))
# liste4.clear()
liste4[:] = []
print(liste4[:])


# mettre une chaine de caractère dans une liste => split avec des éspaces
chaine = "Bonjour à tous"
chaine = chaine.split(" ")
print(chaine)

# mettre une liste en une chaine => joint 
liste5 = ['Coucou', 'à', 'tous']
maChaine = " / ".join(liste5)
print(maChaine)

# /7/ copie d'une liste dans une autre => copy.deepcopy
import copy
listeOrig = ["Arc", "Bouclier", "Tunique"]
listeNouvelle = copy.deepcopy(listeOrig)
print("Liste Ori     ", listeOrig[:])
print("Liste Nouvelle", listeNouvelle[:])
listeNouvelle.append("Potion de mana")
print("Liste Ori     ", listeOrig[:])
print("Liste Nouvelle", listeNouvelle[:])

# /8/ ajouter/concatener une liste à une autre => extend ou +
listeA = ["1", "2", "3"]
listeB = ["toto", "a", "ok"]
print(listeA[:])
# listeA.extend(listeB)
listeA = listeA + listeB
print(listeA[:])

# /9/ parcourir une liste avec le couple (indice , valeur) => enumerate(listeA)
for item in enumerate(listeA):
    print(item)

for numero_indice, valeur_indice in enumerate(listeA):
    print("Element d'indice {} -> {}".format(numero_indice, valeur_indice))
