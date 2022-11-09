from alimata.core.board import Board

from maison.pieces.piece import Piece
from maison.objetsConnecte.lumiere import Lumiere




class Salon(Piece):

    def __init__(self, board: Board) -> None:
        super().__init__()
        self.lumiere = Lumiere(board, 5)

    