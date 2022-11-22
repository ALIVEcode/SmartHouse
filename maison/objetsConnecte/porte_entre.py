from alimata.core.board import Board
from alimata.actuators.servo import Servo



class Porte_entre:
    def __init__(self, board: Board, pin_servo: str) -> None:
        self.__servo = Servo(board=board, pin_=pin_servo)
        self.__servo.move_to(90)
        
    def ouvrir(self):
        self.__servo.move_to(0)

    def fermer(self):
        self.__servo.move_to(90)
