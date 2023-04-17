import os
from nltk.tokenize import RegexpTokenizer

inpfilename = "/home/aziz/Recherche-Information/TP1/collection/"
outpathname = "/home/aziz/Recherche-Information/TP1/collection_tokens/"

def Tokenize(filename):
    file = open(inpfilename+filename,'r')
    f = open (outpathname+filename+".tok",'w')
    words = ""
    while True: #Dans cette boucle, on lit toutes les lignes du fichiers 
        line = file.readline()
        if not line :
            break;
        words +=line #On stocke les lignes lues dans une chaîne de caractères
    file.close()
    tokenizer = RegexpTokenizer('[A-Za-z]\w{1,}') #On ne garde que les mots qui commencent par une lettre et qui ne contiennnent ensuite que des lettres ou des schiffres
    words = tokenizer.tokenize(words)
    for elem in words: #On écrit ces mots dans un autre fichier. Ce fichier sera stocker dans un autre répertoire "collection_tokens"
        f.write(elem.lower()+"\n")
    f.close()


for filename in os.listdir(inpfilename): # On appelle la fonction Tokenize pour tous les fichiers de "collection"
    Tokenize(filename)
   