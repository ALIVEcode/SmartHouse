from abc import ABC, abstractmethod

from alimata.core.board import Board

from maison.objetsConnecte.lumiere import Lumiere
from alimata.sensors.motion import Motion

from time import sleep



class Piece(ABC):

    def __init__(self, board: Board, pin_detecteur_mouvement: str, pin_lumiere: str) -> None:
        self.detecteur_mouvement = Motion(board=board, pin=pin_detecteur_mouvement, on_change=self.__mouvement)
        sleep(0.1)
        self.lumiere = Lumiere(board, pin_lumiere)
        self.__callback = None


    def sur_mouvement(self, fonction) -> None:
        self.__callback = fonction


    def __mouvement(self, motion):
        if self.__callback is not None: # and motion.data
            self.__callback(motion.data)