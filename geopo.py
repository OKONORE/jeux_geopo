from random import randrange

class Chambre:
    def __init__(self):
        self.nom = nom
        self.places = places
        self.pouvoirs = pouvoirs                # "legislatif", "constitutionnel", "executif", "Judiciaire", "relations internationales"
        self.elections = elections
        self.president_chambre = president_chambre
        self.droit_veto = droit_veto            # True False

compteur_id_membres = 0
def id_unique_membre():
    global compteur_id_membres
    compteur_id_membres += 1
    return compteur_id_membres
class Membre:
    def __init__(self, nom, age, parti, salaire,
                loyaute, popularite, talent):
        self.id_membre = id_unique_membre()
        self.nom = nom
        self.age = age
        self.parti = parti
        self.salaire = salaire
        self.loyaute = loyaute
        self.popularite = popularite
        self.talent = talent

compteur_id_parti = 0
def id_unique_parti():
    global compteur_id_parti
    compteur_id_parti += 1
    return compteur_id_parti
class Parti:
    def __init__(self, TAG, nom, adherants, intention_vote,
                membres, leader):
        self.id_parti = id_unique_parti()
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

compteur_id_pays = 0
def id_unique_pays():
    global compteur_id_pays
    compteur_id_pays += 1
    return compteur_id_pays
class Pays:
    def __init__(self, nom:str, population:int, regime_politique, partis_politiques:list):
        self.id_pays = id_unique_pays()
        self.nom = nom                                      # Nom complet du pays
        self.population = population                        # Habitants du pays
        self.richesse = 50                                  # Richesse du pays | 0;29 > Très pauvre | 30;49 > Très pauvre | 50;69 > Modéré | 70;89 > Riche | 90;100 > Très riche |
        self.regime_politique = regime_politique            
        self.partis_politiques = partis_politiques          
        self.bonheur = 50                                   # Bonheur du pays | 0;29 > Très malheureux | 30;49 > Malheureux | 50;69 > Neutres | 70;89 > Heureux | 90;100 > Très heureux |
        self.opinions = Opinions()

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

def creer_membres(nombres, parti):
    membres = []
    for _ in range(nombres):
        membres.append(
            Membre("nom", randrange(18, 60), "parti", randrange(2000, 5000), randrange(1, 10) , randrange(1, 10), randrange(1, 10)))
    return membres

print([x.id_membre for x in creer_membres(5, "oui")])
