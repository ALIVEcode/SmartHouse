from alimata.actuators.led import Led
from alimata.core.board import Board

class Lumiere:
    def __init__(self, board: Board, pin_lumiere: str) -> None:
        self.__led = Led(board, pin_lumiere)

    def allumer(self) -> None:
        self.__led.on()

    def eteindre(self) -> None:
        self.__led.off()

    def toggle(self) -> None:
        self.__led.toggle()