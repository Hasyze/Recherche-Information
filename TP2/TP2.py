from operator import itemgetter
from this import d  
from nltk.stem.porter import *
import json
from math import *
import os

inpfilename = "/home/aziz/RI/TP1/collection_tokens/"
outpathname = "/home/aziz/RI/TP2/collection_tokens/"

def Json (filename,dic):
    with open(filename, 'w') as file:
      json.dump(dic, file)
    file.close()

def Antidico (filename):
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

antidico = Antidico("/home/aziz/RI/TP1/common_words")

voc = {}

def DicoFichier ():
    dicoFichier={}
    stemmer = PorterStemmer() # creation d'un objet stemmer
    for filename in os.listdir(inpfilename):
        file = open(inpfilename+filename,"r")
        dic ={}
        # MotVu =[]
        while True:
            line = file.readline().rstrip('\r\n')
            racine = stemmer.stem(line)
            if not line :
                break
            if (not racine in antidico):
                if(not (racine in voc)):
                    voc[racine] = 0
                if (racine in dic):
                    dic[racine] += 1
                else:
                    dic[racine] = 1
                # if (not(racine in MotVu)):  #preparation prochain TP
                #     MotVu.append(racine)   #preparation prochain TP      
        dicoFichier[filename]=dic
        file.close()
    return dicoFichier

dicoFichier = DicoFichier()


def Idf (word):
    df = 0
    for file in dicoFichier.values():
        if (word in file):
            df += 1
    return log (len(dicoFichier)/df)

for word in voc.keys():
    voc[word] += Idf (word)
    
Json("vocabulaire.json", voc)
    
def Vect (dic):
    vect={}
    for mot in dic:
       vect[mot]=dic[mot]*voc[mot] 
    return vect
    
vecteur={}
for file,dic in dicoFichier.items():
    vecteur[file]= Vect (dic)
    
Json("vecteur.json", vecteur)

def IndexInv (word):
    indice={}
    for file,words in vecteur.items():
        if (word in words):
            indice[file]=words[word]
    return indice

index={}
for word in voc.keys():
    index[word]= IndexInv (word)
    
Json("indexInverse.json", index)

def Norme (file):
    nb = 0
    vec = vecteur[file]
    for word in vec:
        nb += vec[word]**2
    return sqrt(nb)

norme = {}
for file in vecteur:
    norme[file] = Norme(file)  

    
Json("norme.json", norme)
 
# def nb_doc (dic,mot):
#     i = 0
#     for value in dic.values():
#         if (mot in value):
#             i += 1
#     return i
# #1
# antidico = {} #preparation prochain TP
# f = open("/home/aziz/RI/TP2/common_words","r")
# while True:
#         line = f.readline().rstrip('\r\n')
#         if not line :
#             break
#         if (line in antidico):  #preparation prochain TP
#             antidico[line]+=1   #preparation prochain TP
#         else:                  #preparation prochain TP
#             antidico[line] = 1  #preparation prochain TP
# f.close()

# dicoFichier={}
# stemmer = PorterStemmer() # creation d'un objet stemmer
# for i in range (1,3205):
#     file = open(inpfilename+str(i)+".tok","r")
#     listMot = [] #preparation prochain TP
#     while True:
#         line = file.readline().rstrip('\n')
#         if not line :
#             break
#         if (not (line in antidico) and  not(line in listMot)):  #preparation prochain TP
#             listMot.append(stemmer.stem(line))   #preparation prochain TP
#     #dicoFichier[inpfilename+str(i)+".tok"] = listMot
#     dicoFichier["CACM-"+str(i)]=listMot
    # file.close()
  
# #2, 3
# tronc ={}
# l = []
# for key,value in dicoFichier.items():
#     for mot in value:
#         #racine = stemmer.stem(mot) # genere la racine du mot qui est une chaine de caractères
#         if (not (mot in l)):
#             l.append(mot)
#             tronc[mot] = 0

# #4
# for key in tronc.keys():
#     tronc[key]+= log(len(dicoFichier)/nb_doc(dicoFichier,key))
       
#5
# d={}
# for key,value in dicoFichier.items():
#     di={}
#     for mot in value:
#        di[mot]=value.count(mot)*tronc[mot] 
#     d[key]= di

#6
# index={}
# for key in tronc.keys():
#     l={}
#     for k,value in d.items():
#         if ((key in value)):
#         #    l[k]=0
#         #else:
#             l[k]=(value[key])
#     index[key]=l

# with open("vocabulaire.json", 'w') as fp:
#       json.dump(tronc, fp)
# fp.close()

# with open("vecteur.json", 'w') as fi:
#       json.dump(d, fi)
# fi.close()

# with open("index.json", 'w') as f:
#       json.dump(index, f)
# f.close()

    

