from alimata.core.board import Board
from maison.objetsConnecte.sonnette import Sonnette


class PorteEntre:
    def __init__(self, board: Board, pinMoteur: int, pinPiezo: int, pinButton: int) -> None:
        self.sonnette = Sonnette(board, pinPiezo, pinButton)

