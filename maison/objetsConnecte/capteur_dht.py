from alimata.sensors.dht import DHT
from alimata.core.board import Board


class CapteurDHT:
    def __init__(self, board: Board, pin_dht: str) -> None:
        self.__dht = DHT(board, pin_dht, 11)

    @property
    def temperature(self) -> None:
        self.__dht.temperature

    @property
    def humidite(self) -> None:
        self.__dht.humidity