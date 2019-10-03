import time
import board
import digitalio

inter = digitalio.DigitalInOut(board.D7)
inter.direction = digitalio.Direction.INPUT
inter.pull = digitalio.Pull.UP

counter = 0.0
lastTime = 0

while True:
    now = time.monotonic()
    if inter.value:
        counter += 1
    if now > lastTime + 4:
        print("The number of interrupts are:")
        print(counter)
        lastTime = now