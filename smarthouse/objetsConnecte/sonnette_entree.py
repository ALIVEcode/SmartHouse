from threading import Thread
from time import sleep

from alimata.core.board import Board
from alimata.actuators.piezo import Piezo
from alimata.sensors.button import Button


class SonnetteEntree:
    def __init__(self, board: Board, pin_piezo: int, pin_button: int) -> None:
        self.__piezo = Piezo(board, pin_piezo)
        self.button = Button(board, pin_button, invert=True, on_change=self.__pressed)
        self.__callback = None
    

    def sonner(self) -> None:
        print("Ding")
        Thread(target=self.__sonnette_thread).start()


    def sur_clic(self, fonction) -> None:
        self.__callback = fonction

    def __pressed(self, btn : Button) -> None:
        if self.__callback is not None: # and btn.data:
            self.__callback(btn.data)
        
    
    def __sonnette_thread(self) -> None:
        self.__piezo.play_tone(1100)
        sleep(0.4)
        self.__piezo.play_tone(550, 250)