TP1

2.Activer un environnement virtuelle:source venv/bin/activate

4.Geler la configuration: pip freeze > requirements-dev.txt permet de faire une sorte de boite rempli des outil dont le projet a besoin pour fonctionner

partie2 du tp1

1 Lancer l'app grace a uvicorn : uvicorn app.main:app --reload

Partie 4 
4.2

cas 2 

non la fonction n'est pas executer 

le code http retourné est le code 422
le parametre concerné est user id
le type attendu est un int 

4.3
Le paramètre n'est pas obligatoire car on a mis None 

2 Dans notre cas la valeur est toujours accepter car on a mis str peut importe le type il sera toujours convertit en str 



partie 5

Field permet de:
                -exprimer des règles métiers simple
                -documenter les contraintes dans Swagger 
                -centraliser la validation dans le modèle 

1.Pourquoi le champ id n'est il pas présentd ans le modèle UserCreate?
Parce que il n'existe pas encore au moment ou l'utilisateur envoie les données 

2.A quelle moment et par qui l'identifiant d'un utilisateur doit-il etre attribuer?
C'est la base de données qui s'en charge au moment de l'ecriture(insertion)

5.2 

1Pourquoi a t'on defini deux modeles distinct usermodel et usermodelcreate?


Pour séparer les role usermodelcreate c'est ce que l'utilisater a le droit  d'entréer pour s'inscrire c'est les données entrantes 

usermodel c'est ce que le systeme renvoie c'est les donnnées sortante 

2. Pourquoi le champ id n'apparait il pas dans usermodelcreate?

Car l'utilisateur ne peut pas taper lui meme sont id sinon il pourrais ecraser celui d'un utilisateur déjà existant c'est pour la sécutité 

3.A quel moment et par qui l'identifiant id d'un utilisateur est il attribué?

Au moment de la sauvegarde en base de données par le composant le composant qui gere le stockage.

4.Parceque ducoup l'utilisateur devrait deviner quelle id mettre qui n'est pas deja attribuer a un autre utilisateur dans le cas ou on dois entrer un id obligatoirmeent et meme dans le cas se serait optionnel avec none il faudrais ducoup faire de longue condition pour verifier que l'id n'est pas null et sa polluerais le code.

5.Pourquoi n'utilise t'on pas l'heritage entre usermodelcreate et usermodel alors qu'il serait possible de refactoriser certains attributs?

pour la sécurite imaginons que plus tard je veuille donner la possibilité a l'utilisateur d'entrer un mot de passe dans usermodel  create si usermodel herite de usermodelcreate il verra le mot de passe et quand il renverra le profile de l'utilisateur on verra sont mdp ce qui en fait une grosse faille de sécurité.

5.3 
1.POurquoi UserFactory ne dois pas importer FastAPI?

POur sépararer les repsonsabilité fastapi s'occupe du coter web avec les requette get etc... alors que la factory lit des fichiers texte et construit des objets python 

2.Quels seraient les inconvenients si la factory dépendait directement de FastAPI?
 
Cela poserait des problème au niveau des test il faudrait qu'on charge tout le moteur web et sa ralentirais les test de plus si fastAPI fais une mise a jour de sont système la factory peut se mettre a bugger

3 Dans quel autre contexte en dehors d'une API fastapi on pourrrais reutiliser cette factory?

Dans un script en ligne de commande qui permet de compter le nombre d'utilisateur et de generer un pdf 

ou Dans une application de bureau qui permettrai a un agent d'accueil de gérer le utilisateur depuis une interface 

5.5
listez au moins 3 cas de test pertinent pour vérifier le comportement de la factory 

On peut tester le cas ou le json envoyer est parfait et il retourne une liste de model 

Le cas ou le la clé users n'est pas presente ou que la clé est différente de users

Le cas ou une des valeurs est incorrecte par exemple age vaut -10

Quelle est le problème avec le chemin du fichier json factory.create_users("data/users.json")

-Le problme est que le chemin est figé dans le code 

-Le code dois etre changer si on change de machine 

-La configuration est dispersé

Une variable d'environnement est une variable fourni par le système, ou fourni par l'environement d'executtion et elle n'est pas écrite dans le code

Pourquoi on utiliser les fichiers .env ?

Car il permettent il permettent de -centraliser la configuration
                                   -de ne pas modifier le code selon l'environnement
                                   -de ne pas versionner les informations importante 


A quoi sert le setting?

Il permet de ne pas coder en dur et améliore la sa secutité de l'application c'est comme un panneau de configuration 


A quoi sert monkeypatch?

-c'est un outil pytest  
-Il permet de définir une variable d'environnemet pour un test
-Il supprimer une variable d'environnement 
-il permet de garantir que chaque test est isolé et reproductible



