from operator import itemgetter  
from math import *
import os

inpfilename = "/home/aziz/RI/TP1/collection_tokens/"

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


  

# dicoFichier = {} #preparation prochain TP
# My = 0
# M = 0
# for i in range (1,3205):
#     file = open(inpfilename+str(i)+".tok","r")
#     dicoMot = {} #preparation prochain TP
#     while True:
#         line = file.readline().rstrip('\n')
#         if not line :
#             break
        
#         if (line in dicoMot):  #preparation prochain TP
#             dicoMot[line]+=1   #preparation prochain TP
#         else:                  #preparation prochain TP
#             dicoMot[line] = 1  #preparation prochain TP

#         if (line in dico):
#             dico[line]+=1
#         else:
#             dico[line] = 1
#             My +=1
#         M += 1
#     dicoFichier[inpfilename+str(i)+".tok"] = dicoMot
#     file.close()

# top = 1
# for elem in reversed(sorted(dico.items(), key = itemgetter(1))):
#     print (elem)
#     if (top == 10):
#         break
#     top +=1
# print("\n")
# print("M := "+str(M))
# print ("My := "+str(My))
# l = M/(log(My))
# print ("Lambda := "+str(l))