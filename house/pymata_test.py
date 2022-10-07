from pymata_express import pymata_express
import time, sys, asyncio

# instantiate pymata_express
board = pymata_express.PymataExpress()
led_pin = 10


async def main():
    await board.set_pin_mode_digital_output(led_pin)
    while True:
        await board.digital_write(led_pin, True)
        print("ON")
        time.sleep(1)
        await board.digital_write(led_pin, False)
        print("OFF")
        time.sleep(1)

# get the event loop
loop = asyncio.get_event_loop()

try:
    # start the main function
    loop.run_until_complete(main())
except (KeyboardInterrupt, RuntimeError) as e:
    loop.run_until_complete(board.shutdown())
    sys.exit(0)
