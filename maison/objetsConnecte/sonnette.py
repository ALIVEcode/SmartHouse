from threading import Thread
from time import sleep

from alimata.core.board import Board
from alimata.actuators.piezo import Piezo
from alimata.sensors.button import Button


class Sonnette:
    def __init__(self, board: Board, pin_piezo: int, pin_button: int) -> None:
        self.__piezo = Piezo(board, pin_piezo)
        self.button = Button(board, pin_button, invert=True, on_change=self.__pressed)
        self.__callback = None
    

    def ding(self) -> None:
        print("Ding")
        Thread(target=self.__sonnette_thread).start()


    def sur_clic(self, fonction) -> None:
        self.__callback = fonction

    def __pressed(self, btn) -> None:
        if self.__callback is not None and btn.data:
            self.__callback()
        
    
    def __sonnette_thread(self) -> None:
        self.__piezo.playTone(1100)
        sleep(0.4)
        self.__piezo.playTone(550, 250)