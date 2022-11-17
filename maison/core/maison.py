import json
from alimata.core.board import Board

from maison.pieces.salon import Salon
from maison.pieces.salle_de_bain import SalleDeBain
from maison.pieces.cuisine import Cuisine

from maison.objetsConnecte.porte_entre import Porte_entre
from maison.objetsConnecte.sonnette_entre import SonnetteEntre
from maison.objetsConnecte.alarme import Alarme


class Maison:
    def __init__(self) -> None:
        # Load config
        with open("maison/core/config.json", "r") as f:
            config = json.load(f)

        # Initialize board
        self.board = Board()

        # Pieces
        self.salon = Salon(self.board, 
            pin_lumiere=config["salon"]["lumiere"]["pin"], 
            pin_detecteur_mouvement=config["salon"]["detecteur_mouvement"]["pin"])
        
        self.cuisine = Cuisine(self.board,
            pin_lumiere=config["cuisine"]["lumiere"]["pin"],
            pin_detecteur_mouvement=config["cuisine"]["detecteur_mouvement"]["pin"],
            pin_red=config["cuisine"]["lave_vaisselle"]["red_pin"],
            pin_green=config["cuisine"]["lave_vaisselle"]["green_pin"],
            pin_blue=config["cuisine"]["lave_vaisselle"]["blue_pin"])


        self.salle_de_bain = SalleDeBain(self.board, 
            pin_lumiere=config["salle_de_bain"]["lumiere"]["pin"], 
            pin_detecteur_mouvement=config["salle_de_bain"]["detecteur_mouvement"]["pin"], 
            pin_capteur_dht=config["salle_de_bain"]["capteur_dht"]["pin"])


        # Objets connectes sans pieces
        self.porte_entre = Porte_entre(self.board, 
            pin_moteur=config["porte_entre"]["moteur"]["pin"])

        
        self.alarme = Alarme(self.board, 
            pin_piezo=config["alarme"]["piezo"]["pin"])

        self.sonnette_entre = SonnetteEntre(self.board,
            pin_piezo=config["alarme"]["piezo"]["pin"], 
            pin_button=config["sonnette_entre"]["button"]["pin"])


    def start(self, setup_func, loop_func):
        self.board.start(setup_func, loop_func)
        





    
    
