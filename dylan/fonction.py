import os
import time
import sys

def clear_terminal():
    os.system('cls')  # Commande spécifique à Windows


def ecrire_lentement(texte, vitesse=0.05):
    """
    Affiche lentement le texte caractère par caractère.
    
    :param texte: Le texte à afficher.
    :param vitesse: La vitesse entre chaque caractère, en secondes (par défaut 0.1s).
    """
    for char in texte:
        sys.stdout.write(char)
        sys.stdout.flush()  # Force l'écriture immédiate du caractère
        time.sleep(vitesse)  # Attendre un peu avant d'afficher le prochain caractère

# Redéfinir la fonction print pour utiliser ecrire_lentement
print = ecrire_lentement


