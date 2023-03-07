class Chambre:
    def __init__(self, nom, pays, nb_sieges, pouvoirs, nom_election, id_election, electeurs, delai_elections):
        self.nom = nom
        self.pays = pays
        self.nb_sieges = nb_sieges
        self.elus = []
        self.pouvoirs = pouvoirs    # "legislatif", "constitutionnel", "executif", "Judiciaire", "relations internationales"
        self.elections = {"type d'election": nom_election, "electeurs": electeurs, "delai elections": delai_elections}   #{"type d'election": ("Majoritaire à 2 tours", 0)}
        
        def lancer_elections(self):
            def elections_majoritaire_2_tours(n, partis, resultats, carte_electorale, portées_max):
                resultats.append(carte_electorale)
                if points == []:
                    return {
                        "Nombre de cartes": n,
                        "cartes electorale": cartes_electorale,
                        "resultats": resultats,
                            }
                taille, taches = len(carte_electorale)-1, []
                for x, y, logo in points:
                    for x1, y1 in [(1+x, 0+y), (0+x, 1+y), (-1+x, 0+y), (0+x, -1+y)]:
                        if 0 <= x1 <= taille and 0 <= y1 <= taille and carte_electorale[y1][x1] == "" if portées_max >=:
                            carte_electorale[y1][x1] = logo
                            resultats[logo] += 1
                            taches.append((x1, y1, logo))
                return expansion(n+1, partis, resultats, carte_electorale)
            
            
            resultats = dict()
            for nom_parti in partis:
                resultats[nom_parti] = 0 
            COTE = 10
            carte_electorale = [["" for _ in range(COTE)] for _ in range(COTE)]

            
        if self.type_election == "majoritaire deux tours":
            return elections_majoritaire_2_tours(0, parti, resultats, carte_electorale)
        
        else:
            return "erreur, parti inexistant"
        
    def ajouter_elu(self, elu):
        for i, place in enumerate(self.elus):
            if place is None:
                self.elus[i] = elu
                return
        self.elus.append(elu)

    def retirer_elu(self, nom_elu):
        for i, elu in enumerate(self.elus):
            if elu.nom == nom_elu:
                self.elus[i] = None
                return elu
        assert ValueError("ce nom n'est pas dans la liste")


class Membre:
    def __init__(self, nom, age, salaire, loyaute, popularite, talent):
        self.nom = nom
        self.age = age
        self.salaire = salaire
        self.loyaute = loyaute
        self.popularite = popularite
        self.talent = talent

class Parti:
    def __init__(self, nom, nb_adherants, logo_fichier, capitalisme, conservatisme, socialisme, liberalisme):
        self.nom = nom
        self.pays
        self.opinions = {"capitalisme":capitalisme, "socialisme":socialisme, "conservatisme":conservatisme, "liberalisme":liberalisme,} 
        self.logo = os.path.join(logo_fichier)
        self.nb_adherants = nb_adherants
        self.membres = []
        self.salaires = self.calculer_salaires()
        self.leader_id = None
        self.economie = {"Caisse":50000, "Depenses":[], "Revenus":[]}
        
    def calculer_salaires(self):
        return sum([membre.salaire for membre in membres])

    def ajouter_membre(self, membre):
        for i, place in enumerate(self.membres):
            if place is None:
                self.membres[i] = membre
                self.calculer_salaires()
                return
        self.membres.append(membre)
        self.calculer_salaires()

    def retirer_membre(self, nom_membre):
        for i, membre in enumerate(self.membres):
            if membre.nom == nom_membre:
                self.membres[i] = None
                self.calculer_salaires()
                return
        assert ValueError("ce nom n'est pas dans la liste")

    def changer_leader(self, nom_membre):
        for i, membre in enumerate(self.membres):
            if membre.nom == nom_membre:
                self.leader_id = i
                self.membres[i].salaire *= 2
                return
        assert ValueError("ce nom n'est pas dans la liste")
    
class Pays:
    def __init__(self, nom:str, population:int, partis_politiques:list, chambres:list, logo_fichier):
        self.nom = nom                                      # Nom complet du pays
        self.logo = os.path.join(logo_fichier)
        self.population = population                        # Habitants du pays
        self.richesse = 50                                  # Richesse du pays | 0;29 > Très pauvre | 30;49 > Très pauvre | 50;69 > Modéré | 70;89 > Riche | 90;100 > Très riche |
        self.partis_politiques = partis_politiques          
        self.bonheur = 50                                   # Bonheur du pays | 0;29 > Très malheureux | 30;49 > Malheureux | 50;69 > Neutres | 70;89 > Heureux | 90;100 > Très heureux |
        self.opinions = {"capitalisme":50, "socialisme":50, "conservatisme":50, "liberalisme":50,} 
        self.agenda = dict()
        self.constitution = {"Chambres":chambres}

    def nouveau_tour(self):
        bonheur = max(min(round(bonheur + (pays.richesse-50)//10), 100), 0)
        population += round(population * (bonheur-40//1500))
        opinions.update_opinions(self)

    def update_opinions(self):
        self.opinions["capitalisme"]    = max(min(round(self.opinions["capitalisme"] + (self.richesse-50))//10, 100), 0)
        self.opinions["socialisme"]     = max(min(round(self.opinions["socialisme"] - (self.richesse-50))//10, 100), 0)
        self.opinions["liberalisme"]    = max(min(round(self.opinions["liberalisme"] - (self.bonheur-50))//10, 100), 0)
        self.opinions["conservatisme"]  = max(min(round(self.opinions["conservatisme"] + (self.bonheur-50))//10, 100), 0)
        
    def obtenir_portée(self):
        portées_max = 100 * len(self.opinions)
        portées = dict()
        for parti in self.partis_politiques:
            portées[parti.nom] = portées_max
            for opinion in self.opinions:
                portées[parti.nom] -= abs(self.opinions[opinion] - parti.opinions[opinion]) // len(self.opinions)
        return portées
