from operator import itemgetter
from this import d  
from nltk.stem.porter import *
import json
from math import *
import os

inpfilename = "/home/aziz/Recherche-Information/TP1/collection_tokens/"

def Json (filename,dic): #Creation d'un fichier .json contenant un dictionnaire dic
    with open(filename, 'w') as file:
      json.dump(dic, file)
    file.close()

def Antidico (filename): # on construit l'anti-dictionnaire
    f = open(filename,"r")
    antidico ={}
    while True:
        line = f.readline().rstrip('\r\n')
        if not line :
            break
        if not(line in antidico):  
            antidico[line]=1  
    f.close()
    return antidico

#L'anti-dictionnaire
antidico = Antidico("/home/aziz/Recherche-Information/TP1/common_words") 

#Le vocabulaire
voc = {}

def DicoFichier ():
    dicoFichier={} #Dictionnaire des fichiers contenant les dictionnaires de chaque fichier
    stemmer = PorterStemmer() # creation d'un objet stemmer
    for filename in os.listdir(inpfilename):
        file = open(inpfilename+filename,"r")
        dic ={} # Dictionnaire des termes d'un fichier
        while True:
            line = file.readline().rstrip('\r\n')
            racine = stemmer.stem(line) # On génére la racine du terme
            if not line :
                break
            if (not racine in antidico): # On ne met pas les mots qui sont dans l'anti-dictionnaire
                if(not (racine in voc)):
                    voc[racine] = 0 # On met tous les termes qui existent dans le vocabulaire
                if (racine in dic):
                    dic[racine] += 1 # Quand on ajoute un mot au dictionnaire d'un fichier, on incrémente son nombre d'occurences
                else:
                    dic[racine] = 1
        dicoFichier[filename]=dic # On associe à chaque fichier son dictionnaire de termes 
        file.close()
    return dicoFichier

#Dictionnaire des documents
dicoFichier = DicoFichier()


def Idf (word): # On caclule le poids de chaque terme
    df = 0
    for file in dicoFichier.values():
        if (word in file):# Ici, on calcule le nombre de fichiers dans lesquels ce terme apparaît
            df += 1
    return log (len(dicoFichier)/df) #La formule du poids

for word in voc.keys():
    voc[word] += Idf (word)
    
Json("vocabulaire.json", voc)# On écrit le vocabulaire dans un fichier .json
    
def Vect (dic):# On construit le vecteur de chaque fichier à partir de son dictionnaire de ces termes
    vect={}
    for mot in dic:
       vect[mot]=dic[mot]*voc[mot] 
    return vect

#Dictionnaire des vecteurs
vecteur={}
for file,dic in dicoFichier.items():
    vecteur[file]= Vect (dic)
    
Json("vecteur.json", vecteur)# On écrit le dictio dans un fichier .json

def IndexInv (word): # On construit l'index inversé d'un terme à partir du dictionnaire vecteur
    indice={}
    for file,words in vecteur.items():
        if (word in words):
            indice[file]=words[word]
    return indice

#dictionnaire des index inversés
index={}
for word in voc.keys():
    index[word]= IndexInv (word)
    
Json("indexInverse.json", index) # On écrit le dictionnaire index dans un fichier .json

def Norme (file): # On calcule la norme de chaque document à partir de son dictionnaire vecteur
    nb = 0
    vec = vecteur[file]
    for word in vec:
        nb += vec[word]**2
    return sqrt(nb)

#Dictionnaire des normes
norme = {}
for file in vecteur:
    norme[file] = Norme(file)  

Json("norme.json", norme) # On écrit le dictionnaire norme dans un fichier .json