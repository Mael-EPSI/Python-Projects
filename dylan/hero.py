import random

class Creature:
    """Classe de base pour toutes les créatures."""
    def __init__(self, nom, description, pv, ca, type_degats, degats):
        self.nom = nom
        self.description = description
        self.pv = pv
        self.ca = ca  # Classe d'armure, la défense
        self.type_degats = type_degats  # Type de dégâts infligés
        self.degats = degats  # Dés de dégâts (ex : "2d6")
        self.initiative = 0
        self.etats = []  # États actuels (empoisonné, paralysé, etc.)
        self.actions = []  # Actions possibles

    def lancer_initiative(self):
        self.initiative = random.randint(1, 20)
        print(f"{self.nom} lance l'initiative : {self.initiative}")

    def afficher_caracteristiques(self):
        print(f"Nom : {self.nom}\nDescription : {self.description}\nPV : {self.pv}\nCA : {self.ca}\nType de dégâts : {self.type_degats}\nDégâts : {self.degats}\nÉtats : {', '.join(self.etats) if self.etats else 'Aucun'}\n")

    def afficher_actions(self):
        print(f"Actions disponibles pour {self.nom} :")
        for i, action in enumerate(self.actions, 1):
            print(f"{i}. {action.nom}")

    def attaque(self, cible):
        print(f"\n{self.nom} attaque {cible.nom} !")
        jet_attaque = random.randint(1, 20)
        print(f"\nJet d'attaque : {jet_attaque} (CA de {cible.nom} : {cible.ca})")

        if jet_attaque > cible.ca:
            # Touché !
            print(f"L'attaque de {self.nom} touche {cible.nom} !")
            degats_totaux = self.lancer_des(self.degats)

            # Résistance aux dégâts
            if self.type_degats in getattr(cible, 'resistances', []):
                print(f"{cible.nom} résiste aux dégâts {self.type_degats}, dégâts divisés par 2.")
                degats_totaux //= 2

            cible.pv -= degats_totaux
            print(f"{cible.nom} subit {degats_totaux} points de dégâts ({cible.pv} PV restants).")

            if cible.pv <= 0:
                cible.pv = 0
                print(f"{cible.nom} est mort !")
        else:
            print(f"L'attaque de {self.nom} échoue.")

    def lancer_des(self, des):
        # Vérifie si 'des' est un tuple
        if isinstance(des, tuple):
            des = 'd'.join(map(str, des))  # Convertir le tuple en chaîne au format "2d8"
        elif not isinstance(des, str):
            raise ValueError("Le format des dégâts est incorrect")
        
        # Maintenant que 'des' est une chaîne valide, on peut faire le split
        try:
            nb_des, type_de = map(int, des.split('d'))
        except ValueError:
            raise ValueError(f"Le format des dégâts '{des}' est invalide")
        
        # Lancer les dés ou d'autres logiques ici
        degats_totaux = sum(random.randint(1, type_de) for _ in range(nb_des))
        return degats_totaux
        

class Hero(Creature):
    def __init__(self, nom, description, pv, ca, type_degats, degats, arme):
        super().__init__(nom, description, pv, ca, type_degats, degats)
        self.arme = arme  # Arme équipée
        self.inventaire = []  # Objets possédés
        self.actions = [
            Action("Attaque", self.attaque),
            Action("Se soigner", self.se_soigner)
        ]

    def se_soigner(self, cible=None):
        soin = self.lancer_des("2d8")
        self.pv += soin
        print(f"{self.nom} se soigne et récupère {soin} PV ({self.pv} PV actuels).")

    def __str__(self):
        return f"{self.nom} (PV: {self.pv}, CA: {self.ca}, Arme: {self.arme})"

class Monstre(Creature):
    def __init__(self, nom, description, pv, ca, type_degats, degats, resistances):
        super().__init__(nom, description, pv, ca, type_degats, degats)
        self.resistances = resistances  # Types de dégâts auxquels le monstre résiste
        self.actions = [
            Action("Attaque", self.attaque)
        ]

class Action:
    """Représente une action que peut effectuer une créature."""
    def __init__(self, nom, fonction):
        self.nom = nom
        self.fonction = fonction
