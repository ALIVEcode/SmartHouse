from alimata.core.board import Board
from alimata.actuators.lcd import Lcd
from time import sleep


class LCD:
    def __init__(self, board: Board) -> None:
        self.__lcd = Lcd(board=board, adress=0x27, rows=4, cols=20)

    def afficher(self, ligne1: str, ligne2: str, ligne3: str, ligne4: str):
        self.__lcd.quick_print(ligne1, ligne2, ligne3, ligne4)
        sleep(1)


