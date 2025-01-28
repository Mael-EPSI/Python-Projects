import random
from hero import Hero, Monstre
from fonction import clear_terminal
from stock_hero import heros_choisis  


list_hero = [
    Hero(nom="Brutus", description="Un grand gaillard aussi costaud que débile.", pv=50, ca=14, degats=(2, 8), type_degats="Contondant", arme="Épée courte"),
    Hero(nom="Chevalier Guénolé", description="L'écuyer promu chevalier par manque de troupe", pv=32, ca=14, degats=(2, 6), type_degats="Élémentaire", arme="Arc long"),
    Hero(nom="Gaspard", description="Barde enrolé de force qui va séduire les monstres avec sa douce voix", pv=110, ca=16, degats=(2, 8), type_degats="Mental", arme="Baton magique")
]

def choix_perso_hero():
    nombre_heros = int(input("Combien de héros veux-tu jouer ? "))

    for _ in range(nombre_heros):
        print("\nVoici les héros disponibles :")
        for i, hero in enumerate(list_hero, 1):
            print(f"{i}. {hero.nom},\n {hero.description},\n (PV: {hero.pv}, CA: {hero.ca})\n")

        try:
            choix = int(input("\nChoisis le numéro du héros que tu veux : "))
            
            # Vérifier que le choix est dans les indices valides
            if 1 <= choix <= len(list_hero):
                hero = list_hero.pop(choix - 1)
                heros_choisis.append(hero)
                print(f"\n{hero.nom} a été ajouté à votre équipe !")
            else:
                print(f"Numéro de héros invalide. Choisissez un numéro entre 1 et {len(list_hero)}.")

        except ValueError:
            print("Veuillez entrer un nombre valide.")
        except IndexError:
            print("Erreur interne: l'index demandé n'est pas valide.")

    print("\nHéros choisis :")
    for hero in heros_choisis:
        hero.afficher_caracteristiques()

choix_perso_hero()

