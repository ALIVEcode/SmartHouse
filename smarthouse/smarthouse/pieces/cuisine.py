from alimata.core.board import Board


from smarthouse.pieces.piece import Piece

from smarthouse.objetsConnecte.lave_vaisselle import LaveVaisselle





class Cuisine(Piece):

    def __init__(self, board: Board, pin_lumiere: str, pin_detecteur_mouvement: str, pin_red : str, pin_green: str, pin_blue) -> None:
        super().__init__(board= board, pin_detecteur_mouvement= pin_detecteur_mouvement, pin_lumiere=pin_lumiere)

        self.lave_vaisselle = LaveVaisselle(board, pin_red, pin_green, pin_blue)

    