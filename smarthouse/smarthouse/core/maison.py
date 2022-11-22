import json
from alimata.core.board import Board

from smarthouse.pieces.salon import Salon
from smarthouse.pieces.salle_de_bain import SalleDeBain
from smarthouse.pieces.cuisine import Cuisine
from smarthouse.pieces.chambre import Chambre

from smarthouse.objetsConnecte.porte_entre import Porte_entre
from smarthouse.objetsConnecte.sonnette_entre import SonnetteEntre
from smarthouse.objetsConnecte.alarme import Son
from smarthouse.objetsConnecte.lcd import LCD

from time import sleep

class Maison:
    def __init__(self) -> None:
        # Load config
        with open("smarthouse/core/config.json", "r") as f:
            config = json.load(f)

        # Initialize board
        self.board = Board()

        # Pieces
        sleep(0.3)
        self.salon = Salon(self.board, 
            pin_lumiere=config["salon"]["lumiere"]["pin"], 
            pin_detecteur_mouvement=config["salon"]["detecteur_mouvement"]["pin"])
        
        sleep(0.3)
        self.cuisine = Cuisine(self.board,
            pin_lumiere=config["cuisine"]["lumiere"]["pin"],
            pin_detecteur_mouvement=config["cuisine"]["detecteur_mouvement"]["pin"],
            pin_red=config["cuisine"]["lave_vaisselle"]["red_pin"],
            pin_green=config["cuisine"]["lave_vaisselle"]["green_pin"],
            pin_blue=config["cuisine"]["lave_vaisselle"]["blue_pin"])

        sleep(0.3)
        self.salle_de_bain = SalleDeBain(self.board, 
            pin_lumiere=config["salle_de_bain"]["lumiere"]["pin"], 
            pin_detecteur_mouvement=config["salle_de_bain"]["detecteur_mouvement"]["pin"], 
            pin_capteur_dht=config["salle_de_bain"]["capteur_dht"]["pin"])

        sleep(0.3)
        self.chambre = Chambre(self.board,
            pin_lumiere=config["chambre"]["lumiere"]["pin"],
            pin_detecteur_mouvement=config["chambre"]["detecteur_mouvement"]["pin"],
            pin_capteur_dht=config["chambre"]["capteur_dht"]["pin"])

        sleep(0.3)
        # Objets connectes sans pieces
        self.porte_entre = Porte_entre(self.board, 
            pin_servo=config["porte_entre"]["servo"]["pin"])

        sleep(0.3)
        self.son = Son(self.board, 
            pin_piezo=config["alarme"]["piezo"]["pin"])

        sleep(0.3)
        self.sonnette_entre = SonnetteEntre(self.board,
            pin_piezo=config["alarme"]["piezo"]["pin"], 
            pin_button=config["sonnette_entre"]["button"]["pin"])

        sleep(0.3)
        self.lcd = LCD(self.board)

    def start(self, setup_func, loop_func):
        self.board.start(setup_func, loop_func)
        





    
    
