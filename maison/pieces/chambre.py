from alimata.core.board import Board
from maison.pieces.piece import Piece
from maison.objetsConnecte.capteur_dht import CapteurDHT




class Chambre(Piece):

    def __init__(self, board: Board, pin_lumiere: str, pin_detecteur_mouvement: str, pin_capteur_dht: str) -> None:
        super().__init__(board= board, pin_detecteur_mouvement=pin_detecteur_mouvement, pin_lumiere=pin_lumiere)

        self.capteur_dht = CapteurDHT(board, pin_capteur_dht)