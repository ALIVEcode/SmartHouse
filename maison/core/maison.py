from alimata.core.board import Board
from maison.pieces.salon import Salon
from maison.objetsConnecte.porteEntre import PorteEntre

class Maison:
    def __init__(self) -> None:
        self.board = Board()

        #Pieces
        self.salon = Salon(self.board, pinLumiere=5)

        #Objets connectes sans pieces
        self.porteEntre = PorteEntre(self.board, pinMoteur=7, pinPiezo=3, pinButton=6)





    
    
