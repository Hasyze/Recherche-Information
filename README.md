# Recherche-Information
**MAÏDA Léa
KHELIFI Aziz
CATTEAU Pierrick**

Nous allons détaillé les choix que nous avons pris sur sur chacun des 3 TPs qui comportent respectivement sur la loi de Zipf, la constitution de vocabulaire et la recherche de requête dans des documents.

## Loi de Zipf
L'objectif de ce TP est de mettre en pratique la loi de Zipf en manipulant une collection de documents.
- ### Tokenisation des fichiers

Tout d'abord, nous devons découper les fichiers en entrée, qui sont dans le répertoire `collection/`. Pour cela, nous avons utilisé `tokenize_cacm3`. Cette fonction prend en argument un nom d'un fichier `filename`. Elle recupère les mots de ce fichier et ne garde que les mots qui commencent par une lettre et qui ne contiennnent ensuite que des lettres ou des chiffres, grâce à un tokenizer `tokenizer = RegexpTokenizer('[A-Za-z]\w{1,}')`. Puis, nous écrivons ces mots (le résultat précédent) en minuscules, chaque ligne ne contient qu'un seul mot, dans un autre fichier possèdant le même nom que celui du départ avec une extention `.tok` d'un autre répertoire `collection_tokens/`.

__CACM1 (avant tokenization)__
![](https://cdn.discordapp.com/attachments/689438068566261848/1097488462141198397/Capture_decran_du_2023-04-14_01-37-02.png)

__CACM1.tok (après tokenization):__
![](https://cdn.discordapp.com/attachments/689438068566261848/1097488461507854447/Capture_decran_du_2023-04-13_18-16-22.png)


- ### Calcul de la fréquence d’apparition 
Dans cette fonction, nous ouvrons tous les les fichiers du répertoire `collection_tokens` et nous stockons tous les mots lus dans un dictionnaire avec leur nombre d'occurrence. Autrement dit, si un mot existe déjà dans ce dictionnaire, nous incrémentons sa valeur, sinon nous l'ajoutons au dictionnaire.
Cette fonction nous facilite d'effectuer le traitement de ces données par la suite. En effet, nous affichons dans un ordre décroissant les termes de ce dictionnaire selon leurs fréquences d'apparition.

Enfin, nous calculons et affichons la taille de notre dictionnaire $M_y$ et la valeur $λ$ théorique calculée (`λ = M / math.log(My)`) avec `M = Nombre total d’occurrences des mots ` et `My = Nombre total des mots`

__Résultats des calculs des termes les plus fréquents, de la taille My et de la valeur λ__
![](https://cdn.discordapp.com/attachments/689438068566261848/1097488461822439545/Capture_decran_du_2023-04-14_01-36-30.png)


## Constitution de vocabulaire et representation
Le but de ce TP est de construire l'index inversé, le vocabulaire associé à notre corpus et les autres données relatives à l'indexation l'ensemble de documents CACM.
- ### Application de l'anti-dictionnaire
Tout d'abord, nous allons supprimer tous les mots qui sont présents dans l'anti-dictionnaire. Pour cela, il faut commencer par construire l'anti-dictionnaire en appelant la fonction `Antidico (filename)`, qui prend comme argument le nom du fichier (`common_words`) contenant tous les mots de l'anti-dictionnaire. 


- ### Construction du vocabulaire associé à la collection

Une fois l'anti-dictionnaire est contruit, nous pouvons l'appliquer aux mots de la collection afin d'éliminer les mots qui font partie de l'anti-dictionnaire. Nous faisons cela avec la fonction `DicoFichier`, qui renvoie un dictionnaire contenant tous les dictionnaires de chacun des fichiers de la `collection`.
En même parallèle, nous créons un autre dictionnaire qui correcspond au celui du vocabulaire (`voc`) contenant tous les mots de la collection avec leurs nombres d'occurence dans l'ensemble des documents

- ### Calcul des $df_i$ et $idf_i$
Vu que nous avons stockés le vocabulaire de chaque document dans un dictionnaire, cela nous permettra de calculer leur $df$, dans un premier temps, ainsi que leur $idf$ dans un second temps avec cette formule `math.log( N / df )` ($N$ est le nombre total de documents du corpus).

- ### Représentation vectorielle des fichiers : 
Ensuite, nous avons construit la représentation vectorielle de tous les fichiers du corpus. Pour cela, nous avons décidé de les présenter sous la forme du produit $tf$ et $idf$ ,c'est-à-dire sous la forme du poids d'un mot dans le corpus, vu que précédemment nous avons calculé les $idf$ de tous les documents (stockés dans `voc`) , ainsi que les $tf$, correspondant à la fréquence d'apparition des mots dans chaque document (stockés dans `dicoFichier`).

Nous stockons ce vecteur dans le dictionnaire `vecteur` en associant à chaque document, le dictionnaire des poids de chacun de ces mots (grâce à cette formule: $w = tf \times idf$).

- ### Construction de l'index inversé :

Maintenant, nous devons contruire l'index inversé de chaque terme du vocabulaire. En d'autres termes, nous devons créer un dictionnaire où chaque mot du vocabulaire est associé à la liste des documents qui le contiennent.

 Pour cela on parcours l'ensemble des mots du vocabulaire et l'ensemble des fichiers du vecteur afin de construire cet index inversé. On stocke ensuite ce dictionnaire dans le fichier `indexInverse.json`


- ### Calcul de la norme des vecteurs :

Puis, nous allons derterminer la norme du vecteur de chaque document. Pour cela, nous appliquons cette formule: $norme = √(w_i)²$ qui correspond à la racine carrée de la somme des carrées du poids de chaque terme dans le document.


 - ### Stockage dans le fichier .json :

Enfin, nous assurons de stocker tous les dictionnaires associés à le vocabulaire, le vecteur, l'index inversé et la norme de notre collection de documents dans des fichiers `.json` (respectivement dans `vocabulaire.json`, `vecteur.json`, `indexInverse.json` et `norme.json`)


## Recherche et évaluation

L'objectif de ce TP est de développer un modèle vectoriel sur la base de la représentation VSM.  Autrement dit, à partir d'une requête, nous devons afficher et renvoyer les documents permettant de répondre à cette dernière.
Pour cela, nous devons récuperer l'anti-dictionnaire, le vocabulaire, les index inversés ainsi que la norme que nous avons calculés durant le dernier TP et stockés dans des fichiers `.json`. 

Ensuite, nous récupérons la requête souhaitée à partir du terminale. Une fois cela est effectué, nous traitons cette requête. C'est-à-dire que nous procédons à sa tokenization, et nous éliminons tous les mots qui sont présents dans l'anti-dictionnaire, tout en calculant le nombre d'occurence de ces mots dans la requête ($tf$).

Par la suite, nous calculons le $tf*idf$ de chaque mot de notre requête, qui seront stockés dans un dictionnaire représantant le vecteur de cette dernière. De plus, nous calculons la norme de cette requête et nous vérifions qu'elle est non nulle. Si ce n'est pas le cas, cela veut dire qu'il n'y a aucun document qui peut répondre à celle-ci.

Sinon, nous calculons le produit scalaire entre la requête et chaque document avec l'index inversé et nous divisions ces résultats par le produit de la norme de la requête et celle de chaque document pour avoir le score de la requête par chaque document. Les résultats finaux seront stockés dans un dictionnaire pour nous permettre de trier par ordre décroissant de pertinence. 

Enfin, nous affichons les $n$ (un entier que l'utilisateur choisit) documents les plus pertinents correspondant à la requête et nous redemandons une nouvelle requête.

__Résultats de la requête "place"__
![](https://cdn.discordapp.com/attachments/689438068566261848/1097488462434807848/Capture_decran_du_2023-04-15_17-56-44.png)