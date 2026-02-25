# TP1 – 

## 1. Environnement virtuel

### 1.1 Création de l’environnement virtuel

```bash
python -m venv venv
```

### 1.2 Activation de l’environnement virtuel

```bash
source venv/bin/activate
```

### 1.3 Geler la configuration du projet

```bash
pip freeze > requirements-dev.txt
```

Cette commande permet de générer un fichier contenant toutes les dépendances nécessaires au bon fonctionnement du projet.  
On peut comparer cela à une « boîte à outils » contenant tout ce dont le projet a besoin pour fonctionner correctement sur une autre machine.

---

# Partie 2 – Lancement de l’application

Pour démarrer l’application avec Uvicorn :

```bash
uvicorn app.main:app --reload
```

- `app.main` correspond au module Python  
- `app` correspond à l’instance FastAPI  
- `--reload` permet le redémarrage automatique lors des modifications  

---

# Partie 4 – Validation et paramètres

## 4.2 Cas 2

- La fonction n’est pas exécutée  
- Le code HTTP retourné est 422 (Unprocessable Entity)  
- Le paramètre concerné est `user_id`  
- Le type attendu est `int`  

L’erreur se produit car FastAPI valide automatiquement les types.  
Si le type ne correspond pas, la requête est rejetée avant même l’exécution de la fonction.

---

## 4.3 Paramètres optionnels

Le paramètre n’est pas obligatoire car nous avons mis `None` comme valeur par défaut.

Exemple :

```python
name: str | None = None
```

Dans notre cas, la valeur est toujours acceptée car nous avons utilisé `str`.  
Peu importe le type envoyé, il sera converti en chaîne de caractères.

---

# Partie 5 – Modèles Pydantic et Architecture

## 5.1 Field

`Field` permet de :

- Exprimer des règles métier simples  
- Documenter les contraintes dans Swagger  
- Centraliser la validation dans le modèle  

### 1. Pourquoi le champ `id` n’est-il pas présent dans le modèle `UserCreate` ?

Parce qu’il n’existe pas encore au moment où l’utilisateur envoie les données.

### 2. À quel moment et par qui l’identifiant d’un utilisateur doit-il être attribué ?

L’identifiant est attribué par la base de données au moment de l’insertion (écriture).

---

## 5.2 Séparation des modèles

### 1. Pourquoi a-t-on défini deux modèles distincts `UserModel` et `UserModelCreate` ?

Pour séparer les rôles :

- `UserModelCreate` correspond aux données que l’utilisateur a le droit d’entrer lors de son inscription (données entrantes)  
- `UserModel` correspond aux données renvoyées par le système (données sortantes)  

### 2. Pourquoi le champ `id` n’apparaît-il pas dans `UserModelCreate` ?

Car l’utilisateur ne peut pas saisir lui-même son identifiant.  
Sinon, il pourrait écraser celui d’un utilisateur déjà existant, ce qui poserait un problème de sécurité.

### 3. À quel moment et par qui l’identifiant `id` est-il attribué ?

Au moment de la sauvegarde en base de données, par le composant qui gère le stockage.

### 4. Pourquoi ne pas rendre `id` obligatoire ou optionnel ?

Si l’utilisateur devait fournir un `id`, il devrait deviner un identifiant non utilisé.  
Même en le rendant optionnel, il faudrait ajouter de nombreuses vérifications (id nul, id existant, etc.), ce qui compliquerait inutilement le code.

### 5. Pourquoi ne pas utiliser l’héritage entre `UserModelCreate` et `UserModel` ?

Pour des raisons de sécurité.

Si plus tard on ajoute un mot de passe dans `UserModelCreate` et que `UserModel` hérite de celui-ci, le mot de passe pourrait être renvoyé dans les réponses API.  
Cela constituerait une faille de sécurité majeure.

---

## 5.3 Factory et séparation des responsabilités

### 1. Pourquoi `UserFactory` ne doit pas importer FastAPI ?

Pour respecter la séparation des responsabilités :

- FastAPI gère le côté web (requêtes GET, POST, etc.)  
- La factory lit des fichiers JSON et construit des objets Python  

Chaque composant doit avoir une responsabilité claire.

### 2. Quels seraient les inconvénients si la factory dépendait directement de FastAPI ?

- Les tests seraient plus lourds car il faudrait charger le moteur web  
- Les tests seraient plus lents  
- Une mise à jour de FastAPI pourrait casser la factory  
- Le couplage serait trop fort entre les couches  

### 3. Dans quel autre contexte pourrait-on réutiliser cette factory ?

- Dans un script en ligne de commande pour compter les utilisateurs et générer un PDF  
- Dans une application de bureau permettant à un agent d’accueil de gérer les utilisateurs via une interface graphique  

---

## 5.5 Tests de la factory

### Trois cas de test pertinents :

1. Cas nominal : le JSON est correct et retourne une liste de modèles  
2. La clé `users` est absente ou mal nommée  
3. Une valeur est invalide (exemple : âge = -10)  

---

## Problème avec le chemin du fichier JSON

Exemple :

```python
factory.create_users("data/users.json")
```

Problèmes :

- Le chemin est figé dans le code  
- Il faut modifier le code si on change de machine  
- La configuration est dispersée  

---

## Variables d’environnement

Une variable d’environnement est une variable fournie par le système ou par l’environnement d’exécution.  
Elle n’est pas écrite directement dans le code.

### Pourquoi utiliser un fichier `.env` ?

- Centraliser la configuration  
- Ne pas modifier le code selon l’environnement (dev, test, prod)  
- Ne pas versionner des informations sensibles  

---

## À quoi sert `Settings` ?

Il permet d’éviter de coder en dur les paramètres de configuration.  
Il améliore la sécurité et agit comme un panneau de configuration centralisé pour l’application.

---

## À quoi sert `monkeypatch` ?

`monkeypatch` est un outil de pytest.

Il permet :

- De définir une variable d’environnement pour un test  
- De supprimer une variable d’environnement  
- De garantir que chaque test est isolé et reproductible  
