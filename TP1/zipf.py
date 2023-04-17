from operator import itemgetter  
from math import *
import os

inpfilename = "/home/aziz/Recherche-Information/TP1/collection_tokens/"

# Question 3 

dico={}
M = 0 #Le total d’occurrences des mots 

def Zipf(filename):
    file = open(inpfilename+filename,"r")
    global M
    while True:
        line = file.readline().rstrip('\n')
        if not line :
            break
        if (line in dico): #On incremente la valeur du mot s'il est déjà dans dictionnaire
            dico[line]+=1
        else: #Des qu'on lit un nouveau mot, on le rajoute au dictionnaire
            dico[line] = 1
        M+=1
    file.close()

for filename in os.listdir(inpfilename):
    Zipf(filename)  
      
print("Les termes du dictionnaire de mots avec leurs nombres d'occurences :")
for elem in dico:
    print (elem + " : " + str(dico[elem]))

rev_dico = reversed(sorted(dico.items(), key = itemgetter(1))) # Dictionnaire des mots dans l'ordre décroissant d'occurences

# Partie 2

# print("Les termes du dictionnaire par ordre décroissant de fréquences d'apparition :")
# for elem in rev_dico:
#     print (elem[0] + " : " + str(elem[1]))


# Question 4

top = 1
print("Les 10 termes les plus fréquents :")
for elem in rev_dico: #On affiche les 10 mots les plus fréquents avec leurs fréquences d'apparition
    print (str(top)+ "- "+elem[0] + " : " + str(elem[1]))
    if (top == 10):
        break
    top += 1
    
print("La taille du dictionnaire (My) est " + str(len(dico)))

print("La valeur de Lambda théorique calculée est "+str(M/log(len(dico))))
