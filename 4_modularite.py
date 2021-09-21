#coding:utf-8
"""
    Le module est un fichier python (py) qui contient des fonctions
    Importer un module
        exemple: pour calculer le racine carré on doit importer le module math
        import <nom_module>
        from <nom_module> import <nom_fonction>
        import <nom_module> import *
"""

import math 
# from math import *    ==> racineCarre = math.sqrt(100)
# from math import sqr  ==> racineCarre = sqrt(100)

racineCarre = math.sqrt(100)
print(racineCarre)

# Imporrter le module moduleJoueur.py
#--------------------------------------------------------------------------------------
import includes.moduleJoueur as moduleJoueur
moduleJoueur.direAuRevoir()
moduleJoueur.parler("OCI", "Bonjour les recruteurs")

