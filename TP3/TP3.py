from operator import itemgetter  
from nltk.stem.porter import *
from nltk.tokenize import *
import json
from math import *

import sys
sys.path.insert(0, '/home/aziz/RI/TP2')
from TP2 import *

inpfilename = "/home/aziz/RI/TP2/"
filesdirectory = "/home/aziz/RI/TP1/collection_tokens/"
outpathname = "/home/aziz/RI/TP2/collection_tokens/"

stemmer = PorterStemmer()

def GetJson (filename):
	file = open(inpfilename+filename,'r')
	info = json.load(file)
	file.close()
	return info
	
def Traitement (liste_words, antidico):
	clean_words = {}
	for word in liste_words:
		racine = stemmer.stem(word)
		if not (word in antidico) and not (racine in antidico):
			if (racine in clean_words):
				clean_words[racine] += 1
			else:
				clean_words[racine] = 1
	return clean_words
	
antidico = Antidico("/home/aziz/RI/TP1/common_words")

index = GetJson ("indexInverse.json")

voc = GetJson ("vocabulaire.json")

norme = GetJson ("norme.json")

tokenizer = RegexpTokenizer('[A-Za-z]\w{1,}')
requete = input("Saississez une requête: ")

while requete: #Tant que la requête est non vide
    words = tokenizer.tokenize(requete)
    clean_words = Traitement(words, antidico)
    
    # tf*idf
    for word in clean_words:
        if word in voc:
            clean_words[word] *= voc[word]
        else:
            clean_words[word] = 0
            
    nb = 0
    for tf in clean_words.values():
        nb += tf**2
    norme_requete = sqrt(nb)
    
    if norme_requete == 0:
        print ("Cette requête ne peut pas être traitée")
    else:
        #Produit scalaire entre requête et document
        produit_scalaire = {}
        for word in clean_words:
            for file in index[word]:
                if file in produit_scalaire:
                    produit_scalaire[file] += (clean_words[word]*index[word][file])/(norme[file]*norme_requete)
                else:
                    produit_scalaire[file] = (clean_words[word]*index[word][file])/(norme[file]*norme_requete)
                    
        produit_scalaire = reversed(sorted(produit_scalaire.items(), key = itemgetter(1)))
            
        n = int(input("Les n premiers documents les plus pertinents la réponse: "))
        cpt = 1
        for file in produit_scalaire:
            print(str(file[1])+"   "+file[0].split('.')[0])
            if (cpt == n):
                break;
            cpt += 1
        
    requete = input("Saississez une nouvelle requête: ")
        
    
    


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
#     file.close()
  
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
       
# #5
# d={}
# norme ={}
# for key,value in dicoFichier.items():
#     di={}
#     nd = 0
#     for mot in value:
#        di[mot]=value.count(mot)*tronc[mot] 
#        nd += (value.count(mot)*tronc[mot])*(value.count(mot)*tronc[mot] ) 
#     d[key]= di
#     norme[key] = sqrt(nd)

# #6
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

# with open("norme.json", 'w') as f:
#       json.dump(norme, f)
# f.close()

# tokenizer = RegexpTokenizer('[A-Za-z]\w{1,}')
# requete = input("Requete svp !!!")

# while requete: 
#     word = tokenizer.tokenize(requete)
#     stemmer.stem(word)
#     print("je suis la")


    

