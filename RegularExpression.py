import re
import errno


def essaiOuvrir(nom_fichier):
    try:
        f = open(nom_fichier, 'r')
    except (IOError, TypeError):
        if errno.ENOENT:
            print("Entrez un nouveau nom de fichier!")
        elif errno.EPERM:
            print("Changez les permission de votre fichier!")
        elif TypeError:
            print("Type non reconnu!")
        else:
            print("Fichier ouvert avec success.!!")
            
def afficheRegexp(regexp, chaine):
    match = re.findall(regexp, chaine)
    if match != None:
        print(match)
        
        
print("Entrer le nom du fichier: ")
nom_fichier = input()
essaiOuvrir(nom_fichier)
print("Entrer une expression")
regexp = input()
afficheRegexp(regexp, f.read(nom_fichier))