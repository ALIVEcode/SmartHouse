from alimata.actuators.led import Led
from alimata.core.board import Board

class Lumiere:
    def __init__(self, board: Board, pin: int) -> None:
        self.__led = Led(board, pin)

    def allumer(self) -> None:
        self.__led.on()

    def eteindre(self) -> None:
        self.__led.off()

    def etat(self) -> bool:
        return self.__led.is_on()

    def toggle(self) -> None:
        self.__led.toggle()