from alimata.sensors.dht import DHT
from alimata.core.board import Board
from alimata.core.core import DHT_TYPE


class CapteurDHT:
    def __init__(self, board: Board, pin_dht: str) -> None:
        self.__dht = DHT(board, pin_dht, DHT_TYPE.DHT11)

    @property
    def temperature(self) -> float:
        return float(self.__dht.temperature)

    @property
    def humidite(self) -> float:
        return float(self.__dht.humidity)
    
    def to_dict(self):
        return {
            "humidite": self.humidite,
            "temperature": self.temperature
        }