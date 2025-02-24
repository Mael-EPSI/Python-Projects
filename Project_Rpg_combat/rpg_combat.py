import random
import time
from rich.console import Console
from rich.table import Table

console = Console()
# Fonction pour écrire du texte lentement
def slow_print(text, delay=0.05):
    console.print(text)
    time.sleep(delay)

# Définition des types de dégâts
TYPES_DEGATS = ["Contondant", "Tranchant", "Percant", "Magique"]

def saisie_utilisateur(message, type_attendu=int, plage_valeurs=None):
    while True:
        try:
            entree = input(message).strip()  # Suppression des espaces inutiles
            valeur = type_attendu(entree)  # Conversion en type demandé
            if plage_valeurs and valeur not in plage_valeurs:
                raise ValueError("Valeur hors plage autorisée.")
            return valeur
        except ValueError:
            slow_print("[bold red]Entrée invalide, veuillez réessayer.[/bold red]")


class Creature:
    def __init__(self, nom, pv, defense, type_degats):
        self.nom = nom
        self.pv = pv
        self.defense = defense
        self.type_degats = type_degats
        self.initiative = 0

    def lancer_initiative(self):
        self.initiative = random.randint(1, 20)

    def est_vivant(self):
        return self.pv > 0
    
    def attaque(self, cible):
        jet = random.randint(1, 20)
        slow_print(f"[bold yellow]{self.nom} attaque {cible.nom} avec un jet de {jet}![/bold yellow]")
        
        if jet == 20:
            degats = self.calculer_degats() * 2
            slow_print(f"[bold green]Coup critique ! {self.nom} inflige {degats} dégâts à {cible.nom}![/bold green]")
        elif jet == 1:
            degats = self.calculer_degats()
            slow_print(f"[bold red]Échec critique ! {self.nom} s'inflige {degats} dégâts ![/bold red]")
            self.pv -= degats
            return
        elif jet >= cible.defense:
            degats = self.calculer_degats()
            slow_print(f"[bold cyan]Attaque réussie ! {self.nom} inflige {degats} dégâts à {cible.nom}![/bold cyan]")
        else:
            slow_print(f"[bold red]{self.nom} rate son attaque contre {cible.nom} (La cible a {cible.defense} de defense, l'attaque n'as donc pas abouti)![/bold red]")
            return
        cible.pv -= degats
    
    def soigner(self, cible):
        soin = random.randint(5, 15)
        cible.pv += soin
        slow_print(f"[bold green]{self.nom} soigne {cible.nom} et lui rend {soin} PV![/bold green]")
    
    def buff(self, cible):
        bonus = random.randint(1, 5)
        cible.defense += bonus
        slow_print(f"[bold blue]{self.nom} buff {cible.nom}, augmentant sa défense de {bonus} points![/bold blue]")
    
    def debuff(self, cible):
        malus = random.randint(1, 5)
        cible.defense = max(0, cible.defense - malus)
        slow_print(f"[bold red]{self.nom} affaiblit {cible.nom}, réduisant sa défense de {malus} points![/bold red]")
    
    def calculer_degats(self):
        return random.randint(1, 8)

class Heros(Creature):
    def __init__(self, nom, pv, defense):
        arme = choix_arme()
        super().__init__(nom, pv, defense, arme.typedegat)
        self.arme = arme

    def calculer_degats(self):
        nombre_des, faces = self.arme.degatarme
        return sum(random.randint(1, faces) for _ in range(nombre_des))

class Monstre(Creature):
    def __init__(self, nom, pv, defense, type_degats, resistances=[]):
        super().__init__(nom, pv, defense, type_degats)
        self.resistances = resistances

# Liste des armes disponibles
class Arme:
    def __init__(self, nom, degatarme, typedegat):
        self.nom = nom
        self.degatarme = degatarme
        self.typedegat = typedegat

list_arme = [
    Arme(nom="Epée", degatarme=(5, 6), typedegat="Tranchant"),
    Arme(nom="Arc", degatarme=(3, 6), typedegat="Percant"),
    Arme(nom="Hache", degatarme=(1, 8), typedegat="Contondant"),
    Arme(nom="Lance", degatarme=(3, 8), typedegat="Percant"),
    Arme(nom="Caillou", degatarme=(10, 2), typedegat="Magique")
]

def choisir_action(creature, participants):
    slow_print(f"\n{creature.nom}, choisissez une action :")
    actions = ["Attaquer", "Soigner", "Buff", "Debuff"]
    for i, action in enumerate(actions, 1):
        slow_print(f"{i}. {action}")

    choix = saisie_utilisateur("Votre choix : ", int, range(1, len(actions) + 1)) - 1
    cibles = [c for c in participants if c.est_vivant()]

    slow_print("Choisissez une cible :")
    for i, c in enumerate(cibles, 1):
        slow_print(f"{i}. {c.nom} (PV: {c.pv}, Défense: {c.defense})")
    cible = cibles[saisie_utilisateur("Votre choix : ", int, range(1, len(cibles) + 1)) - 1]

    if choix == 0:
        creature.attaque(cible)
    elif choix == 1:
        creature.soigner(cible)
    elif choix == 2:
        creature.buff(cible)
    elif choix == 3:
        creature.debuff(cible)

def generer_monstres_uniques(nb_monstres):
    noms_monstres_disponibles = ["Goblin","Moukiks","Tyranids","Orruk","Serraphon","Necron",]
    monstres = []
    for _ in range(nb_monstres):
        if not noms_monstres_disponibles:
            break  # Stop if there are no more unique names available
        nom = random.choice(noms_monstres_disponibles)
        noms_monstres_disponibles.remove(nom)
        pv = random.randint(10, 30) 
        defense = random.randint(5, 15)
        type_degats = random.choice(TYPES_DEGATS)
        resistances = random.sample(TYPES_DEGATS, k=random.randint(0, 2))
        monstres.append(Monstre(nom, pv, defense, type_degats, resistances))
    return monstres

def tour_de_combat(participants):
    participants.sort(key=lambda x: x.initiative, reverse=True)
    for creature in participants:
        if creature.est_vivant():
            choisir_action(creature, participants)
        
def afficher_stats(participants):
    table = Table(title="Statistiques des combattants (Triés par initiative)")
    table.add_column("Nom", justify="left", style="cyan", no_wrap=True)
    table.add_column("PV", justify="right", style="green")
    table.add_column("Défense", justify="right", style="red")
    table.add_column("Type de dégâts", justify="right", style="magenta")
    table.add_column("Initiative", justify="right", style="yellow")
    
    for p in participants:
        table.add_row(p.nom, str(p.pv), str(p.defense), p.type_degats, str(p.initiative))
    console.print(table)

def choix_arme():
    table = Table(title="Armes Disponibles")
    table.add_column("Numéro", justify="center", style="cyan", no_wrap=True)
    table.add_column("Nom", justify="left", style="yellow", no_wrap=True)
    table.add_column("Dégâts", justify="center", style="red")
    table.add_column("Type de Dégâts", justify="left", style="magenta")
    
    for i, arme in enumerate(list_arme, 1):
        table.add_row(str(i), arme.nom, f"{arme.degatarme[0]}d{arme.degatarme[1]}", arme.typedegat)
    
    console.print(table)
    
    try:
        choix = saisie_utilisateur("\nChoisis le numéro de l'arme que tu veux : ", int, range(1, len(list_arme) + 1))
        if 1 <= choix <= len(list_arme):
            return list_arme.pop(choix - 1)
        else:
            print("Numéro d'arme invalide. Veuillez choisir un numéro correct.")
            return choix_arme()
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return choix_arme()

def combat_tour():
    slow_print("Combien de héros vont combattre ?")
    nb_heros = int(saisie_utilisateur("Nombre de héros : ", int))
    liste_heros = ["Brutus", "Chevalier Guénolé", "Gaspard"]
    heros = []
    for _ in range(nb_heros):
        slow_print("Choisissez un héros parmi :")
        for i, nom in enumerate(liste_heros, 1):
            slow_print(f"{i}. {nom}")
        choix = saisie_utilisateur("Votre choix : ", int, range(1, len(liste_heros) + 1)) - 1
        heros.append(Heros(liste_heros.pop(choix), random.randint(30, 45), random.randint(4, 13)))
    
    niveau = 1
    while any(h.est_vivant() for h in heros):
        slow_print(f"\n--- Niveau {niveau} de la tour ---")
        monstres = generer_monstres_uniques(random.randint(1, 3))
        participants = heros + monstres
        
        for p in participants:
            p.lancer_initiative()
        
        participants.sort(key=lambda x: x.initiative, reverse=True)
        afficher_stats(participants)
        
        while any(m.est_vivant() for m in monstres) and any(h.est_vivant() for h in heros):
            tour_de_combat(participants)
            # Implémentation du tour de combat ici
        
        if all(m.pv <= 0 for m in monstres):
            slow_print(f"[bold green]Les héros ont vaincu tous les monstres du niveau {niveau}![/bold green]")
            niveau += 1
        else:
            slow_print("[bold red]Tous les héros sont morts. Fin de la partie.[/bold red]")
            break




if __name__ == "__main__":
    combat_tour()