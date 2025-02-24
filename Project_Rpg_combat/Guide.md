# 📖 Système de Combat RPG en Python

## 📝 Description
Ce projet est un système de combat RPG textuel en **Python** basé sur la **Programmation Orientée Objet (POO)**. Il a été développé en respectant les consignes initiales, avec une gestion des héros, des monstres et des actions dans un combat **au tour par tour**.
Le jeu propose un mode **progression en tour**, où les joueurs affrontent des monstres à chaque niveau. Ils doivent survivre en utilisant **attaques, soins, buffs et debuffs**.
Lors de la reflexion du projets nous avons decidé de ne pas laisser le choix des monstres a l'utilisateur car nous somme parti du principe que dans un donjon on ne choisi pas vraiment ce qui ci trouve. Alors pour la génération de monstre nous avons choisi de faire un **random** entre 1 et 3 monstre, de plus plus on monte dans les paliers plus les montres sont forts.

**Alors ? Prêt à tenter ce défi ?**

---

## ⚙️ Fonctionnalités Principales

### 🎭 Sélection des Personnages
- Le joueur **choisit le nombre de héros** qui participeront au combat.
- Il sélectionne **chaque héros** parmi une liste préétablie.
- Chaque héros **choisit une arme** avec un type de dégâts spécifique.

### ⚔️ Système de Combat
- Chaque personnage **lance un dé d’initiative** (_1d20_) pour déterminer l’ordre du tour.
- À son tour, une créature peut **attaquer, soigner, utiliser un buff ou un debuff**.
- Les attaques ont des mécanismes de **réussite critique** (_20 = dégâts doublés_) et **échec critique** (_1 = auto-dégâts_).
- Un combat continue **jusqu’à ce que tous les monstres ou tous les héros soient vaincus**.

### 🏆 Progression au sain de la Tour 
- Au debut de chaque jeux, le joueur doit faire la **Sélection de personnage** comme d'écrite au dessus.
- *Le principe est simple*, le joueur a pour but de monter de plus en plus haut dans la tour, pour ca il peut effectuer differents action décrite dans le **Système de combat**. Au debut de chaque niveau de la tour il va tomber sur des montres qui seront généré automatique *(Entre 1 et 3 monstres)*. 

### 🎲 Jets de Dés
- Le jeu utilise différents dés (_1d20 pour les attaques, 3d6 pour certaines armes, etc._).
- Les dégâts sont générés de manière aléatoire en fonction de l’arme et du personnage.

---

## 🚀 Installation et Exécution

### Depuis le fichier Project_DnD.zip
1. **Dézip le fichier / se rendre dedans** :
   ```sh
   cd Project_Rpg_combat
   ```
2. **Installer les dépendances** :
   ```sh
   pip install -r requirements.txt
   ```
3. **Lancer le jeu** :
   ```sh
   python rpg_combat.py
   ```

### Depuis le lien github
1. **Cloner le dépôt** :
   ```sh
   git clone https://github.com/Mael-EPSI/Python-Projects.git
   
   cd Project_Rpg_combat
   ```
2. **Installer les dépendances** :
   ```sh
   pip install -r requirements.txt
   ```
3. **Lancer le jeu** :
   ```sh
   python rpg_combat.py
   ```

---

## 📅 Planning 

- Pour ce projet on a mis en place un planning, pour certaine tache nous avons sur-estimé le temps que ca nous prendrais mais dans l'ensemble nous avons plutot réussis a respecté le temps donner. 
- Voici **Le lien :** *https://trello.com/b/MlGOUbvn/python-project*

---

## ⚒️ Liste des Armes Disponibles

Exemple d'un affichage typique de l'interface que vous prouvez retrouver dans le jeux. 

| Numéro | Nom     | Dégâts  | Type de Dégâts  |
|--------|--------|--------|----------------|
| 1      | Épée   | 5d6    | Tranchant      |
| 2      | Arc    | 3d6    | Percant        |
| 3      | Hache  | 1d8    | Contondant     |
| 4      | Lance  | 3d8    | Percant        |
| 5      | Caillou| 10d2   | Magique        |

---

## 🛡️ Statistiques des Personnages
Chaque personnage possède :
- **Nom** 🎭
- **Points de Vie (PV)** ❤️
- **Défense** 🛡️
- **Type de Dégâts** ⚔️
- **Initiative** 🎲 (_détermine l'ordre du tour_)

---

## 🏹 Exemples d’Affichage

```
--- Niveau 1 de la tour ---
[Statistiques des combattants]

Brutus (PV: 50, Défense: 12, Arme: Épée, Dégâts: 5d6)
Monstre_1 (PV: 20, Défense: 10, Type de Dégâts: Feu)

Brutus attaque Monstre_1 avec un jet de 18!
Attaque réussie ! Brutus inflige 15 dégâts à Monstre_1!
```
---

## Quelques fonctionnalitées décrites, 

1. Gestion d'erreur
```py
   def saisie_utilisateur(message, type_attendu=int, plage_valeurs=None)
```
Dans le code vous verrez cette fonction, cette fonction est la pour gérer la gestion d'erreur, Elle prend en paramettre plusieurs choses comme le type de valeurs, la plage des valeur et la réponse de l'utilisateur. Au lieu de faire directement un **input()** dans notre code nous appelons directement la fonction **saisie_utilisateur()** qui va gérer automatiquent.

2. Génération de monstres
```py
   def generer_monstres_uniques(nb_monstres)
``` 
Cette fonction, comme expliquer au debut permet de générer aléatoirement les monstres de la tour.

3. Affichage des statistiques 
```py
   def afficher_stats(participants)
```
Vous le verrez au debut de chaque Niveau / Palier, c'est un tableau récapitulatifs de qui ce trouve sur le paliers, **PV**, **Défense**, **Types de dégats**, **Initiative**. Le tableau est trié par ordre de passage c'est a dire par celui qui a l'**initiative** la plus élevé. 

---

## 🔮 Idées d’Améliorations
- **Ajout de compétences spéciales** pour chaque classe de héros.
- **Résistances et faiblesses spécifiques** aux monstres.
- **Ajout d’un inventaire et d’objets utilisables** (potions, équipements).
- **Mode multijoueur** permettant à plusieurs joueurs de participer au combat.
- **Faire un systeme de Sauvegarde / Classement** pour pouvoir reprendre notre avancé.

---

## 👨‍💻 Auteurs
- **Ruchaud Maël** - Partie de la fonctionnalité Supplémentaire.
- **Geffroy Thomas** - Gestion de beaucoup d'interface et de demande a l'utilisateur.
- **Tchoumou Erouane** - Systeme de soins de combat et gestion d'erreurs.