from alimata.core.board import Board
from maison.objetsConnecte.sonnette import Sonnette


class Porte_entre:
    def __init__(self, board: Board, pin_moteur: int, pin_piezo: int, pin_button: int) -> None:
        self.sonnette = Sonnette(board, pin_piezo, pin_button)

