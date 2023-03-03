from random import randrange

class Elections:
    def __init__(self):
        self.nom = nom
        self.delai = delai
        self.type_election = type_election  # "majoritaire deux tours"
        self.sieges = sieges
        self.electeurs = electeurs          # "peuple", "/nom de chambre/"
        self.scores = list()
    def lancer_election(self):
                
class Chambre:
    def __init__(self):
        self.nom = nom
        self.places = places
        self.pouvoirs = pouvoirs                # "legislatif", "constitutionnel", "executif", "Judiciaire", "relations internationales"
        self.electeurs = electeurs              # "peuple", "/chambre/"
        self.president_chambre = president_chambre
        self.droit_veto = droit_veto            # True False
        
class Membre:
    def __init__(self, nom, age, parti, salaire,
                loyaute, popularite, talent):
        self.nom = nom
        self.age = age
        self.parti = parti
        self.salaire = salaire
        self.loyaute = loyaute
        self.popularite = popularite
        self.talent = talent

class Parti:
    def __init__(self, nom, adherants, intention_vote, membres, leader):
        self.nom = nom
        self.adherants = adherants
        self.intention_vote = intention_vote
        self.membres = membres
        self.salaires = self.calculer_salaires()
        self.leader_id = leader
        self.caisse = 50000
        self.revenu = adherants
        self.depenses = salaires
        self.balance = revenu - depenses
        
    def calculer_salaires(self):
        return sum([membre.salaire for membre in membres])

class Opinions:
    def __init__(self):
        self.capitalisme = 50
        self.socialisme = 50
        self.liberalisme = 50
        self.conservatisme = 50
    
    def update_opinions(self, pays):
        self.capitalisme    = max(min(round(capitalisme + (pays.richesse-50))//10, 100), 0)
        self.socialisme     = max(min(round(socialisme - (pays.richesse-50))//10, 100), 0)
        self.liberalisme    = max(min(round(liberalisme - (pays.bonheur-50))//10, 100), 0)
        self.conservatisme  = max(min(round(conservatisme + (pays.bonheur-50))//10, 100), 0)

class Pays:
    def __init__(self, nom:str, population:int, regime_politique, partis_politiques:list):
        self.nom = nom                                      # Nom complet du pays
        self.population = population                        # Habitants du pays
        self.richesse = 50                                  # Richesse du pays | 0;29 > Très pauvre | 30;49 > Très pauvre | 50;69 > Modéré | 70;89 > Riche | 90;100 > Très riche |
        self.partis_politiques = partis_politiques          
        self.bonheur = 50                                   # Bonheur du pays | 0;29 > Très malheureux | 30;49 > Malheureux | 50;69 > Neutres | 70;89 > Heureux | 90;100 > Très heureux |
        self.opinions = Opinions()    
        self.agenda = None
        self.constitution = {"Régime politique":"Democratie", "Chambres":[], 
        
    def nouveau_tour(self):
        bonheur = max(min(round(bonheur + (pays.richesse-50)//10), 100), 0)
        population += round(population * (bonheur-40//1500))
        opinions.update_opinions(self)

###########################

def sauvegarder(sauvegarde, data):
    with open(sauvegarde + ".pickles", "rw+b") as fichier:
        file.write(data)
    f.close()
    return

def charger(sauvegarde):
    with open(sauvegarde + ".pickles", "r") as fichier:
        data = file.read()
    f.close()
    return data
