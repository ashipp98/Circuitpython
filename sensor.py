import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D2, echo_pin=board.D3)
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
while True:
    try:
        dist = sonar.distance
        if dist < 20:
            red = simpleio.map_range(dist, 5, 20, 255, 0)
            led.fill((int(red), 0, 0))
        if dist > 20:
            green = simpleio.map_range(dist, 20, 35, 0, 255)
            led.fill((0, int(green), 0))
        if dist < 1000:
            print(sonar.distance)
            time.sleep(0.1)
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)