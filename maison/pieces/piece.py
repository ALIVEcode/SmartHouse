from abc import ABC, abstractmethod

from alimata.core.board import Board

from maison.objetsConnecte.lumiere import Lumiere
from alimata.sensors.motion import Motion




class Piece(ABC):

    def __init__(self, board: Board, pin_detecteur_mouvement: str, pin_lumiere: str) -> None:
        self.detecteur_mouvement = Motion(board, pin_detecteur_mouvement, on_change=self.__mouvement)
        self.lumiere = Lumiere(board, pin_lumiere)


    def sur_mouvement(self, fonction) -> None:
        self.__callback = fonction


    def __mouvement(self, motion: Motion):
        if self.__callback is not None and motion.data:
            self.__callback()