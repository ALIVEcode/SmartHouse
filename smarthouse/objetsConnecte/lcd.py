from alimata.core.board import Board
from alimata.actuators.lcd import Lcd


class LCD:
    def __init__(self, board: Board) -> None:
        self.__lcd = Lcd(board=board, adress=0x27, rows=4, cols=20)


    def afficher(self, ligne1: str, ligne2: str = ""):
        '''Quickly prints 1 to 2 lines on the LCD'''
        self.__lcd.home()
        self.__lcd.print(ligne1)
        self.__lcd.set_cursor(0, 1)
        self.__lcd.print(ligne2)
