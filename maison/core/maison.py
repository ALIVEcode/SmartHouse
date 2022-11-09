from alimata.core.board import Board
from maison.pieces.salon import Salon
from maison.objetsConnecte.porte_entre import Porte_entre

class Maison:
    def __init__(self) -> None:
        self.board = Board()

        #Pieces
        self.salon = Salon(self.board, pin_lumiere=5)

        #Objets connectes sans pieces
        self.porte_entre = Porte_entre(self.board, pin_moteur=7, pin_piezo=3, pin_button=6)





    
    
