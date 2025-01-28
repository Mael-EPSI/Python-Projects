import random
from hero import Hero, Monstre
from fonction import clear_terminal, print
from stock_hero import heros_choisis

niveau_tour = 1
multiplicateur_monstre = 2

def equipe_hero():
    """
    Affiche les caractéristiques de l'équipe actuelle de héros.
    """
    print("\nÉquipe actuelle :")
    for hero in heros_choisis:
        hero.afficher_caracteristiques()

def creer_monstre(niveau_tour):
    """
    Crée un monstre basé sur le niveau actuel de la tour.
    """

    choice_nom = ["Goblin","Moukiks","Tyranids","Orruk","Serraphon","Necron"]


    nom = random.choice(choice_nom)
    description = "Une créature mystérieuse et dangereuse."
    pv = random.randint(10, 20) * niveau_tour  # Points de vie augmentent avec le niveau
    ca = random.randint(10, 15)  # Classe d'armure aléatoire
    type_degats = random.choice(["Contondant", "Perforant", "Magique", "Feu", "Glace"])  # Type aléatoire
    degats = f"{random.randint(1, 4)}d{random.randint(6, 12)}"  # Exemple : "2d8" ou "1d10"
    resistances = random.sample(["Feu", "Glace", "Acide", "Foudre", "Contondant"], random.randint(0, 3))  # 0 à 3 résistances

    # Création du monstre
    monstre = Monstre(nom, description, pv, ca, type_degats, degats, resistances)
    print(f"\n\nUn monstre apparait :\n- Nom {monstre.nom} \n- Pv : {monstre.pv}, \n- CA : {monstre.ca}")
    print(f"\n- Type de dégâts : {monstre.type_degats}")
    print(f"\n- Dégâts : {monstre.degats}")
    print(f"\n- Résistances : {', '.join(monstre.resistances) if monstre.resistances else 'Aucune'}")
    return monstre

def generer_monstres(niveau_tour):
    """
    Génère une liste de monstres en fonction du niveau de la tour.
    """
    nb_monstres = random.randint(1, niveau_tour + 1)  # Exemple : au niveau 3, entre 1 et 4 monstres
    print(f"\nVous affrontez {nb_monstres} monstre(s) au niveau {niveau_tour} de la tour.")
    return [creer_monstre(niveau_tour) for _ in range(nb_monstres)]

def tour():
    """
    Gère un tour de combat contre les monstres.
    """
    global niveau_tour
    global multiplicateur_monstre

    clear_terminal()
    print(f"Vous vous situez au niveau {niveau_tour} de la tour sur 5.")
    equipe_hero()

    # Génération des monstres pour ce niveau
    monstres = generer_monstres(niveau_tour)

    # Combat jusqu'à ce que tous les monstres ou les héros soient éliminés
    while monstres and heros_choisis:
        for monstre in monstres[:]:  # On itère sur une copie pour permettre de retirer les monstres morts
            input("\n\n Appuyez sur Enter pour passer au combat.")
            clear_terminal()
            print(f"\nCombat contre {monstre.nom} (PV : {monstre.pv}, CA : {monstre.ca})")

            # Les héros attaquent le monstre
            for hero in heros_choisis:
                hero.attaque(monstre)
                if monstre.pv <= 0:
                    print(f"{monstre.nom} a été vaincu !")
                    monstres.remove(monstre)
                    break  # Passe au prochain monstre

            # Si tous les monstres sont vaincus, terminer le combat
            if not monstres:
                print(f"\nTous les monstres au niveau {niveau_tour} ont été vaincus !")
                break
                    
            # Les monstres restants attaquent les héros
            if monstres:
                cible = random.choice(heros_choisis)
                monstre.attaque(cible)
                if cible.pv <= 0:
                    print(f"{cible.nom} a été tué !")
                    heros_choisis.remove(cible)

            # Fin si plus de héros vivants
            if not heros_choisis:
                print("\nTous les héros ont été tués ! Vous avez perdu la partie.")
                return

    # Préparation pour le tour suivant
    niveau_tour += 1
    multiplicateur_monstre *= 1.2  # Augmentation de la difficulté
    if niveau_tour > 5:
        print("\nVous avez atteint le sommet de la tour et gagné la partie !")
        return

    input("Appuyez sur Enter pour continuer au tour suivant...")
    clear_terminal()
    tour()

# Lancer le premier tour
tour()
