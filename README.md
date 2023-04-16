# Recherche-Information
**MAÏDA Léa
KHELIFI Aziz
CATTEAU Pierrick**

Nous allons détaillé les choix que nous avons pris sur sur chacun des 3 TPs qui comportent respectivement sur la loi de Zipf, la constitution de vocabulaire et la recherche de requête dans des documents.

## Loi de Zipf
L'objectif de ce TP est de mettre en pratique la loi de Zipf en manipulant une collection de documents.
### Tokenisation des fichiers

Tout d'abord, nous devons découper les fichiers en entrée, qui sont dans le répertoire `collection/`. Pour cela, nous avons utilisé `tokenize_cacm3`. Cette fonction prend en argument un nom d'un fichier `filename`. Elle recupère les mots de ce fichier et ne garde que les mots qui commencent par une lettre et qui ne contiennnent ensuite que des lettres ou des chiffres, grâce à un tokenizer `tokenizer = RegexpTokenizer('[A-Za-z]\w{1,}')`. Puis, nous écrivons ces mots (le résultat précédent) en minuscules, chaque ligne ne contient qu'un seul mot, dans un autre fichier possèdant le même nom que celui du départ avec une extention `.tok` d'un autre répertoire `collection_tokens/`.

#### EXEMPLES ET IMAGES

### Calcul de la fréquence d’apparition (fichier TP1_Zipf)
Dans cette fonction, nous ouvrons tous les les fichiers du répertoire `collection_tokens` et nous stockons tous les mots lus dans un dictionnaire avec leur nombre d'occurrence. Autrement dit, si un mot existe déjà dans ce dictionnaire, nous incrémentons sa valeur, sinon nous l'ajoutons au dictionnaire.
Cette fonction nous facilite d'effectuer le traitement de ces données par la suite. En effet, nous affichons dans un ordre décroissant les termes de ce dictionnaire selon leurs fréquences d'apparition.

Enfin, nous calculons et affichons la taille de notre dictionnaire `My` et la valeur `λ` théorique calculée (`λ = M / math.log(My)`) avec `M = Nombre total d’occurrences des mots ` et `My = Nombre total des mots`

#### EXEMPLES ET IMAGES

## TP2
#### EXEMPLES ET IMAGES

## Recherche et évaluation

L'objectif de ce TP est de développer un modèle vectoriel sur la base de la représentation VSM.  Autrement dit, à partir d'une requête, nous devons afficher et renvoyer les documents permettant de répondre à cette dernière.
Pour cela, nous devons récuperer l'anti-dictionnaire, le vocabulaire, les index inversés ainsi que la norme que nous avons calculés durant le dernier TP et stockés dans des fichiers `.json`. 

Ensuite, nous récupérons la requête souhaitée à partir du terminale. Une fois cela est effectué, nous traitons cette requête. C'est-à-dire que nous procédons à sa tokenization, et nous éliminons tous les mots qui sont présents dans l'anti-dictionnaire, tout en calculant le nombre d'occurence de ces mots dans la requête ($tf$).

Par la suite, nous calculons le $tf*idf$ de chaque mot de notre requête, qui seront stockés dans un dictionnaire représantant le vecteur de cette dernière. De plus, nous calculons la norme de cette requête et nous vérifions qu'elle est non nulle. Si ce n'est pas le cas, cela veut dire qu'il n'y a aucun document qui peut répondre à celle-ci.
Sinon, nous calculons le produit scalaire entre la requête et chaque document avec l'index inversé et nous divisions ces résultats par le produit de la norme de la requête et celle de chaque document pour avoir le score de la requête par chaque document. Les résultats finaux seront stockés dans un dictionnaire pour nous permettre de trier par ordre décroissant de pertinence.  

Enfin, nous affichons les $n$ (un entier que l'utilisateur choisit) documents les plus pertinents correspondant à la requête et nous redemandons une nouvelle requête.


### IMAGES ET EXEMPLES