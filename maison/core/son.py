from threading import Thread
from alimata.core.board import Board
from alimata.actuators.piezo import Piezo
from time import sleep

class Son:
    def __init__(self, board: Board, pin: int) -> None:
        self.__piezo = Piezo(board, pin)
        self.__currentAlarmOn = False

    def sonnerAlarme(self) -> None:
        if not self.__currentAlarmOn:
            self.__currentAlarmOn = True
            Thread(target=self.__alarmeThread, daemon=True).start()
            
    def stopperAlarme(self) -> None:
        self.__currentAlarmOn = False
        self.__piezo.stopTone()


    def __alarmeThread(self) -> None:
        while self.__currentAlarmOn:
            self.__piezo.playTone(1000)
            sleep(0.2)
            self.__piezo.stopTone()
            sleep(0.2)