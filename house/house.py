""" WORK IN PROGRESS """


from aliot.aliot_obj import AliotObj
from house_state import HouseState
from pymata_express import pymata_express
import time, sys, asyncio

# instantiate pymata_express
#board = pymata_express.PymataExpress()
led_pin = 10

""" Aliot connection """
house = AliotObj("house")

# the state of your object should be defined in this class
house_state = HouseState(light_on=True)

def start():
    # write the code you want to execute once your object is connected to the server
    pass



async def main():
    #await board.set_pin_mode_digital_output(led_pin)
    while True:
        house_state.light_on = True
        #await board.digital_write(led_pin, house_state.light_on)
        print("ON")
        time.sleep(1)
        house_state.light_on = False
        #await board.digital_write(led_pin, house_state.light_on)
        print("OFF")
        time.sleep(1)


house.on_start(callback=main)
house.run(async_mode=True)  # connects your object to the sever


