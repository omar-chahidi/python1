print("bonjours Omar")

# comment
print("bonjours CHAHIDI")

"""
comment
"""
print("bonjours OCI")

# Variables
agePersonne = 37
prix = 12.3
print("L'age de la personne est de", agePersonne , "et le prix HT est de" , prix, "euros")
phrase = "L'age de la personne est de {} et le prix HT est de {} euros"
print(phrase.format(agePersonne, prix))

# input() -> fct pour lire au clavier
prixHT = input("Entre le prix HT svp :")
prixHT = int(prixHT)
prixTTC = prixHT + (prixHT*20/100)
print("Le prix TCC est de :", prixTTC)
