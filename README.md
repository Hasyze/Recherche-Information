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
Enfin, nous calculons et affichons la taille de notre dictionnaire `My` et la valeur `λ` théorique calculée (`M / math.log(My)`) avec `M = Nombre total d’occurrences des mots ` et `My = Nombre total des mots`

#### EXEMPLES ET IMAGES