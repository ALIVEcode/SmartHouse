from alimata.core.board import Board

from smarthouse.pieces.piece import Piece


class Salon(Piece):

    def __init__(self, board: Board, pin_lumiere: str, pin_detecteur_mouvement: str) -> None:
        super().__init__(board=board, pin_detecteur_mouvement=pin_detecteur_mouvement, pin_lumiere=pin_lumiere)

    def to_dict(self):
        return {}
    