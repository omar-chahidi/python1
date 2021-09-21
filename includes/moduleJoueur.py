#coding:utf-8
"""
Module joueur
"""

def parler(personnage, message):
    print("{} => {}".format(personnage, message))

def direAuRevoir():
    print("Au revoir ...")


"""
    Comment tester le module avant de l'utiliser dans le programe principale "4_modularite.py"
    Tout simplement il faut isoler ce module
    Pour tester ce modue il faut 
        1/ cd includes
        2/ python moduleJoueur.py
"""
if __name__ == "__main__":
    print("PHASE DE TEST DU MODULE moduleJoueur.py")
    direAuRevoir()
    parler("OCI", "Bonjour les recruteurs")