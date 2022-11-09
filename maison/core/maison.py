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

        #Pieces
        self.salon = Salon(self.board, 
            pin_lumiere=config["salon"]["pins"]["lumiere"], 
            pin_detecteur_mouvement=config["salon"]["pins"]["detecteur_mouvement"])
        
        self.cuisine = Cuisine(self.board,
            pin_lumiere=config["cuisine"]["pins"]["lumiere"],
            pin_detecteur_mouvement=config["cuisine"]["pins"]["detecteur_mouvement"],
            pin_red=config["cuisine"]["pins"]["red"],
            pin_green=config["cuisine"]["pins"]["green"],
            pin_blue=config["cuisine"]["pins"]["blue"])


        self.salle_de_bain = SalleDeBain(self.board, 
            pin_lumiere=config["salle_de_bain"]["pins"]["lumiere"], 
            pin_detecteur_mouvement=config["salle_de_bain"]["pins"]["detecteur_mouvement"], 
            pin_capteur_dht=config["salle_de_bain"]["pins"]["capteur_dht"])


        #Objets connectes sans pieces
        self.porte_entre = Porte_entre(self.board, 
            pin_moteur=config["porte_entre"]["pins"]["moteur"])
        
        self.alarme = Alarme(self.board, 
            pin_piezo=config["alarme"]["pins"]["piezo"])

        self.sonnette_entre = SonnetteEntre(self.board,
            pin_piezo=config["sonnette_entre"]["pins"]["piezo"], 
            pin_button=config["sonnette_entre"]["pins"]["button"])


    def start(self, setup_func, loop_func):
        self.board.start(setup_func, loop_func)
        





    
    
