# README

Voici le repo du projet e4 R7 sur la reconnaissance d'utilisateur de smartwatch.

## Pour commencer

Pour cloner le repo, utilisez la commande suivante:

```bash
git clone https://github.com/appollo30/projet-e4.git
````

Vous devrez alors avoir accès au projet.

Ensuite, créez votre propre branche pour travailler sur le projet. C'est ici que vous pourrez faire vos modifications.

```bash
git checkout -b votre-prenom
```

Pour vérifier que vous êtes bien sur votre branche, utilisez la commande suivante:

```bash
git branch
```

Normalement vous devriez voir une astérisque devant votre branche.
![alt text](image.png)

Vous pouvez alors commencer à travailler sur le projet.

Quand vous avez fini de travailler sur votre branche, vous pouvez ajouter vos modifications avec la commande suivante:

```bash
git add .
git commit -m "Ce que j'ai fait comme modifications"
git checkout main
git merge votre-prenom
```

Vous pouvez alors push vos modifications sur le repo avec la commande suivante:

```bash
git push origin main
```

N'oubliez pas enfin de retourner sur votre branche avec la commande suivante:

```bash
git checkout votre-prenom
```

N'OUBLIEZ PAS DE PUSH QUAND VOUS AVEZ FINI DE TRAVAILLER SUR VOTRE BRANCHE.

S'il y a des problèmes de conflits, zebi on est livrés à nous-même on va devoir se demerder. Au pire juste demandez-moi (leo) et j'essaierai de vous aider.

Quand vous revenez sur le projet après un certain temps, vous pouvez mettre à jour votre branche avec la commande suivante:

```bash
git pull origin main
```

## Structure du projet

Le projet est divisé en plusieurs parties:

- `data`: les données du projet
- `src`: le code source du projet
- `tests_personnels`: les tests personnels de chacun

### DATA

Voir `data/README.md` pour plus d'informations.

### SRC

Le code du projet, hésitez pas à feuilleter ce qu'il y a déjà avant d'essayer de développer quelque chose, ça se trouve quelqu'un a déjà fait ce que vous voulez faire.

Pour télécharger les dépendances du projet, utilisez la commande suivante:

```bash
pip install -r requirements.txt
```

Pour lancer le projet, utilisez la commande suivante:

```bash
python main.py
```

### Tests personnels

Soyez libres de faire ce que vous voulez dans ce dossier, c'est votre espace de travail personnel. Rien de ce qui est dans ce dossier ne sera push sur le repo.

## Derniers conseils

Hésitez pas à faire des commit à chaque fois que vous avez fini une fonctionnalité plutôt qu'une fois avec uen grosse quantité de taf, ça permet de garder une trace de ce que vous avez fait. Plus vous en faites fréquemment, moins de chances vous avez d'avoir des conflits (et plus ils seront faciles à résoudre).

Si vous avez du mal à vous servir de git, hésitez pas à me demander (leo) je vous aiderai avec plaisir.
