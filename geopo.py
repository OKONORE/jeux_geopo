from random import randrange
import os
import sys
import pathlib
import pickle
import dearpygui.dearpygui as dpg

sys.setrecursionlimit(999999)

if sys.platform == "win32":
    user_directory = os.path.join(pathlib.Path.home(), "AppData/", "Roaming/")
elif sys.platform == "linux":
    user_directory = os.path.join(pathlib.Path.home(), ".local/", "share/")
elif sys.platform == "darwin":
    user_directory = os.path.join(pathlib.Path.home(), "Library/", "Application Support/")

##

class Chambre:
    def __init__(self, name: str, country: str, nb_seats: int, pouvoirs: list, name_election: str,
                 electeurs: str, delai_elections: int):
        self.name = name
        self.country = country
        self.nb_seats = nb_seats
        self.elus = []
        self.pouvoirs = pouvoirs    # "legislatif", "constitutionnel", "executif", "Judiciaire", "relations internationales"
        self.elections = {"type d'election": name_election, "electeurs": electeurs, "delai elections": delai_elections}   #{"type d'election": ("Majoritaire à 2 tours", 0)}
        
    def lancer_elections(self, country_opinions: list, country_partis: list):
        def first_past_the_post_voting(partis):
            """
            Return a dict with the result of a First-past-the-post voting election
            """
            results = dict()
            # portées_max = self.country.obtenir_portée()
            nb_opinions = len(parti.opinion)
            for parti in partis:
                results[parti.name] = sum([100-abs(country_opinions[key]-parti[key])/nb_opinions for key in parti.opinion])
            sum_results = sum([results[key] for key in results])
            for parti in partis:
                results[parti.name] = round(results[parti.name]/sum_results*randrange(100-10, 100), 2)
            return results | {"abstention": sum([results[key] for key in results])}
        
        if self.elections["type d'election"] == "Scrutin uninominal majoritaire à un tour":
            return first_past_the_post_voting(country_partis)

        elif self.elections["type d'election"] == "Election directe à 2 tour":
            turn = first_past_the_post_voting(country_partis)
            turn = sorted([tuple(turn[key], key) for key in turn], reverse=True)[:2]
            if len(turn) >= 2: # 2 party
                turn = first_past_the_post_voting([])
                    

        elif self.elections["type d'election"] == "Election indirecte à 1 tour":
            return

        elif self.elections["type d'election"] == "Election indirecte à 2 tour":
            return

        else:
            raise ValueError("lancer_elections(): erreur, type d'election inexistant")

    def ajouter_elu(self, elu):
        for i, place in enumerate(self.elus):
            if place is None:
                self.elus[i] = elu
                return
        self.elus.append(elu)

    def retirer_elu(self, name_elu):
        for i, elu in enumerate(self.elus):
            if elu.name == name_elu:
                self.elus[i] = None
                return elu
        raise ValueError("ce name n'est pas dans la liste")

class Membre:
    def __init__(self, name: str, age: int, salary: int, loyalty: int, popularity: int, talent: int):
        self.name = name
        self.age = age
        self.salary = salary
        self.loyalty = loyalty
        self.popularity = popularity
        self.talent = talent

class Parti:
    def __init__(self, name: str, country, nb_adherent: int, logo, capitalism: int, liberalism: int):
        capitalism, liberalism = max(min(capitalism, 100), 0), max(min(liberalism, 100), 0)
        self.name = name
        self.country = country
        self.opinions = {
            "capitalism": capitalism,
            "socialism": 100 - capitalism,
            "conservatism": 100 - liberalism,
            "liberalism":liberalism,
            }
        self.logo = logo  # os.path.join(logo_fichier)
        self.nb_adherent = nb_adherent
        self.members = []
        self.nb_members = 0
        self.salarys = self.sum_salarys()
        self.leader = None
        self.economy = {"Caisse":50000, "Depenses":[], "Revenus":[]}
        
    def sum_salarys(self):
        return sum([membre.salary for membre in self.members])

    def is_a_member(self, member_name):
        return member_name in [membre.name for membre in self.members]

    def add_member(self, membre):
        self.members.append(membre)
        self.nb_members += 1
        self.salarys = self.sum_salarys()
        
    def retirer_membre(self, member_name: str):
        """
        Remove a member with self.name == 'member_name' from the party members
        """
        for i, name in enumerate([membre.name for membre in self.members]):
            if name == member_name:
                if i < self.nb_members - 1:
                    self.members[i] = self.members.pop()
                else:
                    self.members.pop()
                self.nb_members -= 1
                self.salarys = sum_salarys()
                return True
        raise ValueError("This member does not exist")

    def change_leader(self, member_name):
        for name in [membre.name for membre in self.members]:
            if member_name == name:
                self.leader = member_name
        raise ValueError("This member does not exist")

class country:
    def __init__(self, name : str, population : int, partis_politiques : list, chambres : list, logo):
        self.name = name                                      # name complet du country
        self.logo = logo #os.path.join(logo_fichier)
        self.population = population                        # Habitants du country
        self.richesse = 50                                  # Richesse du country | 0;29 > Très pauvre | 30;49 > Très pauvre | 50;69 > Modéré | 70;89 > Riche | 90;100 > Très riche |
        self.partis_politiques = partis_politiques          
        self.bonheur = 50                                   # Bonheur du country | 0;29 > Très malheureux | 30;49 > Malheureux | 50;69 > Neutres | 70;89 > Heureux | 90;100 > Très heureux |
        self.opinions = {"capitalism":50, "socialism":50, "conservatism":50, "liberalism":50,} 
        self.agenda = dict()
        self.constitution = {"Chambres":chambres}

    def nouveau_tour(self):
        bonheur = max(min(round(bonheur + (country.richesse-50)//10), 100), 0)
        population += round(population * (bonheur - 40//1500))
        opinions.update_opinions(self)

    def update_opinions(self):
        self.opinions["capitalism"]    = max(min((self.opinions["capitalism"] + (self.richesse-50))//10, 100), 0)
        self.opinions["socialism"]     = max(min((self.opinions["socialism"] - (self.richesse-50))//10, 100), 0)
        self.opinions["liberalism"]    = max(min((self.opinions["liberalism"] - (self.bonheur-50))//10, 100), 0)
        self.opinions["conservatism"]  = max(min((self.opinions["conservatism"] + (self.bonheur-50))//10, 100), 0)
        
    def obtenir_portée(self):
        portées_max = 50 * len(self.opinions)
        portées = dict()
        for parti in self.partis_politiques:
            portées[parti.name] = max((100-sum([abs(parti.opinions[opinion] - self.opinions[opinion]) for opinion in parti.opinions]) // len(self.opinions)) / 100, 0.02)
        return portées

    def chambres_selon_pouvoir(self, pouvoir: list):
        resultat = list()
        for chambre in self.constitution["Chambres"]:
            if pouvoir in chambre.pouvoirs:
                resultat.append()
        return resultat

###########################

def print_liste(liste):
    for i, ligne in enumerate(liste):
        print(i, "\t", *ligne, sep="")

def chercher_element(name, list: list):
    for element in liste:
        if element.name == name:
            return element

def membre_aleatoire(self):
    return Membre("name", randrange(18, 60), randrange(2000, 6000), *[randrange(0, 11) for _ in range(3)])

def quit():
    dpg.stop_dearpygui()
    exit()

def rien():
    pass

def option_menu():
    dpg.show_item("Menu_Options")

def play():
    pass

def create_file(value, file_path):
    pickle.dump(value, open(user_directory+"PolitiSim/"+file_path, "wb"), protocol=pickle.HIGHEST_PROTOCOL)

def save_settings(sender, app_data, values):
    settings = dict()
    for element in values:
        settings[element] = dpg.get_value(element)
    create_file(settings, "PolitiSim.settings")

def get_settings():
    default_settings = {
        'FullScreen?': False,
        'VSync?': False,
        'AZERTY?': False,
        'QWERTY?': False,
        'personalized?': False,
        'WindowedFullScreen?': False,
        'Resolution?': '1280x720',
        "Viendra": None,
    }
    if os.path.exists(user_directory+"PolitiSim/PolitiSim.settings"):
        settings_temp = pickle.load(open(user_directory+"PolitiSim/PolitiSim.settings", "rb"))
        if hash(str(sorted(([x for x in default_settings])))) == hash(str(sorted(([x for x in settings_temp])))):
            return settings_temp
        else:
            os.remove(user_directory+"PolitiSim/PolitiSim.settings")
    return default_settings

def check_1_only(sender, app_data, user_data):
    dpg.set_value(sender, value=True)
    for element in user_data:
        if element != sender:
            dpg.set_value(element, value=False)

#####################

def main():
    global settings, WIDTH, HEIGHT
    settings = get_settings()
    WIDTH, HEIGHT= map(int, settings["Resolution?"].split("x"))
    BACKGROUND_COLOR = (0, 100, 200)

    dpg.create_context()
    dpg.create_viewport(title='PolitiSim', resizable=False, vsync=True, clear_color=BACKGROUND_COLOR, width=WIDTH, height=HEIGHT)
    dpg.setup_dearpygui()


    with dpg.texture_registry(show=False):
        width, height, channels, data = dpg.load_image(os.path.join("data/", "PolitiSim_white.png"))
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="img_PolitiSim_white")

    with dpg.window(label="Titre du jeu", tag="Titre", autosize=True, no_close=True, no_move=True, no_collapse=True, no_background=True, no_title_bar=True, pos=(WIDTH//3.25, HEIGHT//20)):
        dpg.add_image("img_PolitiSim_white", tag="tag_img_PolitiSim_white", pos=(0, 0))

    with dpg.window(label="Menu Principal", tag="menu_principal", autosize=True, no_close=True, no_move=True, no_collapse=True, pos=(WIDTH//3, HEIGHT//3)):       
        for args in [("Jouer", play), ("Tutoriel", rien), ("Options", lambda: dpg.configure_item("Menu_Options", show=True)), ("Crédits", lambda: dpg.configure_item("Menu_Credits", show=True)), ("Quitter", quit)]:
            dpg.add_button(tag="Button_menu_"+args[0], arrow=False, label=args[0], callback=args[1], width=WIDTH//3, height=HEIGHT//15)
        
    # ----> Menu Crédits

    with dpg.window(label="Crédits", tag="Menu_Credits", modal=True, show=False,  no_resize=True, pos=(WIDTH//3, HEIGHT//3), width=WIDTH//3+10, autosize=True):
        with dpg.child_window(height=50):
            dpg.add_text("OKONORE")
        with dpg.child_window(height=50):
            dpg.add_text("Ferwyou")

    # ----> Menu Options

    with dpg.window(label="Menu Options", tag="Menu_Options", modal=True, show=False,  no_resize=True, no_open_over_existing_popup=False, pos=(WIDTH//3, HEIGHT//3)):
        dpg.add_separator()
        all_options_elements = []
        dpg.add_text("Paramètres d'Écran:", bullet=True)
        with dpg.group(horizontal=True):
            screen_check_box = [("FullScreen?", "Plein Ecran"), ("WindowedFullScreen?", "Fenêtré"), ("VSync?", "VSync")]  
            all_options_elements += [tag for tag, _ in screen_check_box] + ["Resolution?"]             
            for i, args in enumerate(screen_check_box):
                dpg.add_checkbox(tag=args[0], label=args[1], default_value=settings[args[0]], indent=(WIDTH//3//3-5)*i)
        dpg.add_text("Résolution:")
        resolutions = sorted([(1920, 1080), (1366, 768), (1280, 720)])
        dpg.add_listbox(([str(x) + "x" + str(y) for x, y in resolutions]), tag="Resolution?", width=WIDTH//3, default_value=settings["Resolution?"])

        dpg.add_separator()
        dpg.add_text("Paramètres de touches:", bullet=True)
        with dpg.group(label="Touches", horizontal=True):
            keys_check_box = [("AZERTY?", "Preset AZERTY"), ("QWERTY?", "Preset QWERTY"), ("personalized?", "Personalisé")]
            all_options_elements += [tag for tag, _ in keys_check_box]
            for i, args in enumerate(keys_check_box):
                dpg.add_checkbox(tag=args[0], label=args[1], default_value=settings[args[0]], callback=check_1_only, user_data=[tag for tag, _ in keys_check_box], indent=(WIDTH//3//3-5)*i)
        
        dpg.add_text("Raccourcis Personalisés:", bullet=True)
        with dpg.table(header_row=True, label="Raccourcis Personalisés"):
            dpg.add_table_column(label="Action")
            dpg.add_table_column(label="Raccourci")

            actions = ["Viendra",]
            all_options_elements += actions
            for action in actions:
                with dpg.table_row():
                    dpg.add_text(action)

        dpg.add_separator()
        with dpg.group(horizontal=True):
            dpg.add_button(label="Fermer", callback=lambda: dpg.hide_item("Menu_Options"), width=WIDTH//3//2-5)
            dpg.add_button(label="Appliquer", callback=save_settings, user_data=all_options_elements, width=WIDTH//3//2-5)
    
    # ----> Menu Resolution

    ##############

    if settings["FullScreen?"] and not settings["WindowedFullScreen?"]:
        dpg.toggle_viewport_fullscreen()
    else:
        dpg.show_viewport(maximized=settings["FullScreen?"] and settings["WindowedFullScreen?"])
    dpg.start_dearpygui()
    dpg.destroy_context()

## Init

def initialisation():
    if not os.path.exists(user_directory+"PolitiSim/"): os.makedirs(user_directory+"PolitiSim/")
    if not os.path.exists(user_directory+"PolitiSim/Saves"): os.makedirs(user_directory+"PolitiSim/Saves")

initialisation()
main()
