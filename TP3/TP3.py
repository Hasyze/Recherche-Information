from operator import itemgetter  
from nltk.stem.porter import *
from nltk.tokenize import *
import json
from math import *

import sys
sys.path.insert(0, '/home/aziz/Recherche-Information/TP2')
from TP2 import Antidico

inpfilename = "/home/aziz/Recherche-Information/TP2/"

stemmer = PorterStemmer()

def GetJson (filename): #Une fonction pour récupèrer le dictionnaire d'un fichier .json
	file = open(inpfilename+filename,'r')
	info = json.load(file)
	file.close()
	return info
	
def Traitement (liste_words, antidico): #Une fonction qui permet de construire le dictionnaire des termes de la requête , après filtrage par l'anti-dictionnaire, avec leur nombre d'occurences 
	clean_words = {}
	for word in liste_words:
		racine = stemmer.stem(word)
		if not (word in antidico) and not (racine in antidico):
			if (racine in clean_words): # On incrémente le nombre d'occurences
				clean_words[racine] += 1
			else:
				clean_words[racine] = 1
	return clean_words

#On récupère l'anti-dictionnaire grâce à la fonction Antidico du TP2
antidico = Antidico("/home/aziz/Recherche-Information/TP1/common_words")

#L'index inversé
index = GetJson ("indexInverse.json")

#Le vocabulaire
voc = GetJson ("vocabulaire.json")

#Les normes des fichiers 
norme = GetJson ("norme.json")

tokenizer = RegexpTokenizer('[A-Za-z]\w{1,}')
requete = input("Saississez une requête: ")

while requete: #Tant que la requête est non vide
    words = tokenizer.tokenize(requete)
    clean_words = Traitement(words, antidico)
    
    # On calcule tf*idf
    for word in clean_words:
        if word in voc:
            clean_words[word] *= voc[word]
        else:
            clean_words[word] = 0
            
    # On calcule la norme de la requête        
    nb = 0
    for tf in clean_words.values():
        nb += tf**2
    norme_requete = sqrt(nb)
    
    if norme_requete == 0:
        print ("Cette requête ne peut pas être traitée")
    else: #Si la requête est non nulle
        
        #On calcule les produits scalaires entre requête et les documents du corpus
        # Et on calcule en même temps le score de la requête et les documents
        produit_scalaire = {}
        for word in clean_words:
            for file in index[word]:
                if file in produit_scalaire:
                    produit_scalaire[file] += (clean_words[word]*index[word][file])/(norme[file]*norme_requete)
                else:
                    produit_scalaire[file] = (clean_words[word]*index[word][file])/(norme[file]*norme_requete)
        
        # Dictionnaire des documents dans l'ordre décroissant des scores            
        produit_scalaire = reversed(sorted(produit_scalaire.items(), key = itemgetter(1)))
            
        n = int(input("Les n premiers documents les plus pertinents: "))
        cpt = 1
        for file in produit_scalaire: # On affiche les n premiers documents les plus pertinents la réponse
            print(str(file[1])+"   "+file[0].split('.')[0])
            if (cpt == n):
                break;
            cpt += 1
        
    requete = input("Saississez une nouvelle requête: ") #On redemande une nouvelle requête
 