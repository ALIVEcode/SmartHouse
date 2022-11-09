from threading import Thread
from time import sleep

from alimata.core.board import Board
from alimata.actuators.piezo import Piezo
from alimata.sensors.button import Button


class Sonnette:
    def __init__(self, board: Board, pinPiezo: int, pinButton: int) -> None:
        self.__piezo = Piezo(board, pinPiezo)
        self.button = Button(board, pinButton, invert=True)
        self.__callback = None
    

    def ding(self) -> None:
        print("Ding")
        Thread(target=self.__sonnetteThread).start()


    def surClic(self, fonction) -> None:
        self.__callback = fonction
        self.button.on_change(self.__pressed)

    def __pressed(self, btn) -> None:
        if self.__callback is not None:
            if btn.data:
                self.__callback()
        
    
    def __sonnetteThread(self) -> None:
        self.__piezo.playTone(1100)
        sleep(0.4)
        self.__piezo.playTone(550, 250)