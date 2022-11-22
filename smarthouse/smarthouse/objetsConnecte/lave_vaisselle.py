from threading import Thread
from time import sleep
from alimata.core.board import Board
from alimata.actuators.ledRGB import LedRGB




class LaveVaisselle:
    def __init__(self, board: Board, pin_red: str, pin_green: str, pin_blue: str) -> None:
        self.__led_rgb = LedRGB(board, pin_red, pin_green, pin_blue)
        self.__working = False
        self.__led_rgb.rgb = (255, 0, 0)
    
    def commencer(self):
        if not self.__working:
            self.__working = True
            Thread(target=self.__workingThread).start()

    def __workingThread(self):
        self.__led_rgb.rgb = (255, 255, 0)
        sleep(10)
        self.__led_rgb.rgb = (0, 255, 0)
        sleep(5)
        self.__working = False
        self.__led_rgb.rgb = (255, 0, 0)
