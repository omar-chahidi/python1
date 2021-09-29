#codin:utf-8


"""
    + Modes d'ouverture:
        r   : lecture seule
        w   : écriture avec remplacement
        a   : écriture avec ajout en fin de fichier
        x   : lecture et écriture
        r + : lecture / écriture dans un même fichier 

    + ouvrir un fichier => open()
    + fermer un fichier => close()
    + récupérer le contenue d'un fichier => read(), readline(), readlines()
    + avec "with" on va ouvrir le fichier en lecture seule et on ne va pas utilser la fonction close pour fermer le fichier 
        elle se fait en automatique
    + Ecriture dans un fichier txt => write()
    + Ecriture /enregistrer une information dans un fichier binaire => dump() c'est à dire une copie
    + récupérer une information depuis un fichier binaire => load()
"""

"""
# ouvrir fichier en lecture seule
fic = open("docs/lireCeFichier.txt", "r")

# récupérer le contenue d'un fichier
content = fic.read()
print(content)
#line = fic.readline()
#print("ligne ", line)
#line = fic.readlines()
#print(line)

# fermer fichier 
fic.close()


"""

with open("docs/lireCeFichier.txt", "r") as fic:
    content = fic.read()
    print(content)
    #Pas besoin de fermer le fichier avec with


if fic.closed:
    print("Fichier fermé")
else:
    print("Fichier encore ouvert")
#print(content)

# Ecriture dans un fichier
with open("docs/remplirCeFichier.txt", "w") as fic2:
    nombre = 15
    fic2.write(str(nombre))
    fic2.write("\nBonjour")


# Enregistre un objet dans un fichier
class Player:
    def __init__(self, name, level):
        self.name =name
        self.level = level
    
    def whoAmai(self):
        print("{} ({})".format(self.name, self.level))

player1 = Player("Omar", 10)
player1.whoAmai()

# Ecriture dans un fichier texte
with open("docs/remplirCeFichier.txt", "w") as fic3:
    nombre = 15
    fic3.write(str(nombre))
    fic3.write("\nBonjour")
    fic3.write("\n{} ({})".format(player1.name, player1.level))

# Ecriture /enregistrer une information dans un fichier binaire
import pickle
with open("docs/players.data", "wb") as fic4Binaire:
    record = pickle.Pickler(fic4Binaire)
    record.dump(player1)

print("---------------")
# récupérer une information depuis un fichier binaire
with open("docs/players.data", "rb") as fic4Binaire:
    get_record = pickle.Unpickler(fic4Binaire)
    player_one = get_record.load()
player_one.whoAmai()
