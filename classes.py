class Chambre:
    def __init__(self, nom, pays, nb_sieges, pouvoirs, nom_election, id_election, electeurs, delai_elections):
        self.nom = nom
        self.pays = pays
        self.nb_sieges = nb_sieges
        self.elus = []
        self.pouvoirs = pouvoirs                # "legislatif", "constitutionnel", "executif", "Judiciaire", "relations internationales"
        self.elections = {"type d'election": nom_election, "electeurs": electeurs, "delai elections": delai_elections)   #{"type d'election": ("Majoritaire à 2 tours", 0)}
        
        def lancer_elections(self):
            resultats = [] # [ nbframes, [frames], 
            def elections_majoritaire_2_tours(carte_electorale, partis)
                if points == []:
                    return carte_electorale
                taille, taches = len(carte_electorale)-1, []
                for x, y, logo in points:
                    for x1, y1 in [(1+x, 0+y), (0+x, 1+y), (-1+x, 0+y), (0+x, -1+y)]:
                        if 0 <= x1 <= taille and 0 <= y1 <= taille and carte_electorale[y1][x1] == None:
                            carte_electorale[y1][x1] = logo
                            taches.append((x1, y1, logo))
                return expansion(liste, taches)
            
        if self.type_election == "majoritaire deux tours":
            return elections_majoritaire_2_tours()
        
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
    def __init__(self, nom, nb_adherants, logo_fichier):
        self.nom = nom
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


class Opinions:
    def __init__(self):
        self.capitalisme    = 50
        self.socialisme     = 50
        self.liberalisme    = 50
        self.conservatisme  = 50
    
    def update_opinions(self, pays):
        self.capitalisme    = max(min(round(capitalisme + (pays.richesse-50))//10, 100), 0)
        self.socialisme     = max(min(round(socialisme - (pays.richesse-50))//10, 100), 0)
        self.liberalisme    = max(min(round(liberalisme - (pays.bonheur-50))//10, 100), 0)
        self.conservatisme  = max(min(round(conservatisme + (pays.bonheur-50))//10, 100), 0)


class Pays:
    def __init__(self, nom:str, population:int, partis_politiques:list, chambres:list, logo_fichier):
        self.nom = nom                                      # Nom complet du pays
        self.logo = os.path.join(logo_fichier)
        self.population = population                        # Habitants du pays
        self.richesse = 50                                  # Richesse du pays | 0;29 > Très pauvre | 30;49 > Très pauvre | 50;69 > Modéré | 70;89 > Riche | 90;100 > Très riche |
        self.partis_politiques = partis_politiques          
        self.bonheur = 50                                   # Bonheur du pays | 0;29 > Très malheureux | 30;49 > Malheureux | 50;69 > Neutres | 70;89 > Heureux | 90;100 > Très heureux |
        self.opinions = Opinions()    
        self.agenda = dict()
        self.constitution = {"Chambres":chambres}

    def nouveau_tour(self):
        bonheur = max(min(round(bonheur + (pays.richesse-50)//10), 100), 0)
        population += round(population * (bonheur-40//1500))
        opinions.update_opinions(self)
