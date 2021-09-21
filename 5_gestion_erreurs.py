#coding:utf-8

ageUtilisateur = input("Entrez votre âge ? ")

try:
    ageUtilisateur = int(ageUtilisateur)
except:
    print("Votre âge non valide !")
else:
    print("Votre âge est de", ageUtilisateur)
finally:
    print("FIN DU PROGRAMME ....")
    