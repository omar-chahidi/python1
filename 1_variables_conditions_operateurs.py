print("bonjours Omar")

# comment

"""
    1/ Variables
"""


agePersonne = 37
prix = 12.3
print("L'age de la personne est de", agePersonne , "et le prix HT est de" , prix, "euros")
phrase = "L'age de la personne est de {} et le prix HT est de {} euros"
print(phrase.format(agePersonne, prix))

# input() -> fct pour lire au clavier
"""
prixHT = input("Entre le prix HT svp :")
prixHT = int(prixHT)
prixTTC = prixHT + (prixHT*20/100)
print("Le prix TCC est de :", prixTTC)
"""

"""
    2/ opérateurs de comparaison et conditions
    opérateurs  
        == 
        != 
        < ou <=
        > ou >=
    conditions multiples
        and (et)
        or (ou)
        in (dans)  - not in (pas dans) 
    mots clé des conditions
        if / elif / else
"""
identifiant = "oci"
motDePasse  = "123"

print("Interface de connexion")
idUser = input("Entrez votre identifiant : ")
pwdUsr = input("Entrez votre mot de passe : ")
ageUser= input("Entrez votre âge : ")
ageUser = int(ageUser)

if idUser == identifiant and pwdUsr == motDePasse:
    print("Vous êtes connecté", idUser)
    #if ageUser > 0 and ageUser <= 100:
    if 0 < ageUser <= 100:
        print("Votre age est validé")
    else:
        print("Votre âge est NON validé")
elif idUser != identifiant and pwdUsr == motDePasse: 
    print("Login non correcte", idUser)
elif idUser == identifiant and pwdUsr != motDePasse:
    print("Mot de passe non correcte", idUser)
else:
    print("Login et mot de passe non correcte", idUser)




