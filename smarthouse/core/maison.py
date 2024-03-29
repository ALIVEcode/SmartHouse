import json
from alimata.core.board import Board

from smarthouse.pieces.salon import Salon
from smarthouse.pieces.salle_de_bain import SalleDeBain
from smarthouse.pieces.cuisine import Cuisine
from smarthouse.pieces.chambre import Chambre

from smarthouse.objetsConnecte.porte_entree import PorteEntree
from smarthouse.objetsConnecte.sonnette_entree import SonnetteEntree
from smarthouse.objetsConnecte.alarme import Son
from smarthouse.objetsConnecte.lcd import LCD

from time import sleep


class Maison:
    def __init__(self) -> None:
        # Load config
        with open("smarthouse/smarthouse/core/config.json", "r") as f:
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
        self.porte_entree = PorteEntree(self.board, 
            pin_servo=config["porte_entree"]["servo"]["pin"])

        sleep(0.3)
        self.son = Son(self.board, 
            pin_piezo=config["alarme"]["piezo"]["pin"])

        sleep(0.3)
        self.sonnette_entre = SonnetteEntree(self.board,
            pin_piezo=config["alarme"]["piezo"]["pin"], 
            pin_button=config["sonnette_entree"]["button"]["pin"])

        sleep(0.3)
        self.lcd = LCD(self.board)

    def start(self, setup_func, loop_func):
        self.board.start(setup_func, loop_func)

    def to_dict(self):
        return {
            "chambre": self.chambre.to_dict(),
            "salle_de_bain": self.salle_de_bain.to_dict(),
            "cuisine": self.cuisine.to_dict(),
            "salon": self.salon.to_dict(),
        }
    
    def as_doc(self, document_name="document"):
        doc = {}
        data = self.to_dict()

        def recursive_as_doc(data: dict, current_prefix: str):
            for key, value in data.items():
                if isinstance(value, dict):
                    doc[f"{current_prefix}/{key}"] = {}
                    recursive_as_doc(value, f"{current_prefix}/{key}")
                else:
                    doc[f"{current_prefix}/{key}"] = value

        recursive_as_doc(data, f"/{document_name}")
        return doc
    