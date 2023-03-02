from random import randrange

class Pays:
    def __init__(self, TAG, nom, population, richesse,
                regime_politique, partis_politiques, bonheur, 
                opinions,):
        self.TAG = TAG
        self.nom = nom
        self.population = population
        self.richesse = richesse
        self.regime_politique = regime_politique
        self.partis_politiques = partis_politiques
        self.bonheur = bonheur
        self.opinions = opinions

def Membre:
    def __init__(self, id_membre, nom, age, parti, salaire
                loyaute, popularite, talent, travail):
        self.id_membre = id_membre
        self.nom = nom
        self.age = age
        self.parti = parti
        self.salaire = salaire
        self.loyaute = loyaute
        self.popularite = popularite
        self.talent = talent
        self.travail = travail
        
        
class Parti:
    def __init__(self, TAG, nom, adherants, intention_vote
                membres, leader):
        self.TAG = TAG
        self.nom = nom
        self.adherants = adherants
        self.intention_vote = intention_vote
        self.membres = membres
        self.salaire = self.calculer_salaires()
        self.leader_id = leader
        
    def calculer_salaires(self):
        return sum([membre.salaire for membre in membres])

compteur_id_membres = 0

def creer_membres(nombres, parti):
    membres = []
    for _ in range(nombres):
        membres.append(
            Membre(compteur_id_membre, "nom", randrange(18, 60), 
            parti, randrange(2000, 5000), randrange(1, 10) , randrange(1, 10), 
            randrange(1, 10)))
