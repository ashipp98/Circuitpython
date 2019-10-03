import board
import analogio

led = analogio.AnalogOut(board.A0)
led.value = 0
led.value = 65535
led.value = 50000

10000 / 65535 * 3.3
0.5035477225909819
50000 / 65535 * 3.3
2.517738612954909

def dac_value(volts):
    return int(volts / 3.3 * 65535)

while True:
    led.value = 65000 #dac_value(2.5)