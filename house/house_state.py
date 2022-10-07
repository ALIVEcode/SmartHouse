from dataclasses import dataclass
from aliot.state import AliotObjState


@dataclass
class HouseState(AliotObjState):
    # write the different properties of your object
    light_on: bool
