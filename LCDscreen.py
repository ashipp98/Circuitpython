# importing necessary libraries
import board
#import neopixel
import time
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from lcd.lcd import CursorMode

# defining both button_alt, button_ud, and button_red as DigitalInOut objects (as buttons
# that increase/decrease value, change modifier, and reset mod and num to 1 and 0 respectively)
button_alt = DigitalInOut(board.D6)
button_alt.direction = Direction.INPUT
button_alt.pull = Pull.UP

button_ud = DigitalInOut(board.D5)
button_ud.direction = Direction.INPUT
button_ud.pull = Pull.UP

button_res = DigitalInOut(board.D4)
button_res.direction = Direction.INPUT
button_res.pull = Pull.UP

# defining lcd as an LCD object
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)

# list that the mod button will cycle through
mods = [1, 2, 5, 10, -1, -2, -5, -10]

# number that is being increased/decreased
num = 0
m = 0

# the variable mod is whichever index of the mods list that m is currently on
mod = mods[m]

# toggles so the buttons cannot be held
toggle1 = 0
toggle2 = 0

while True:

    # resetting cursor, printing number + variable number, "Modifier" and mod
    lcd.set_cursor_pos(0,0)
    lcd.print("Number: " + str(num))
    lcd.set_cursor_pos(1,0)
    lcd.print("Modif.: " + str(mod))

    # changing the number value
    if not button_alt.value and toggle1 == 0:
        toggle1 = 1
        x = len(str(num))
        num += mod
        y = len(str(num))
	# clearing the screen if the number has changed between 9 and 10, 99 and 100, etc.
	# so that we don't have a leftover ones place
        if x > y or y > x:
            lcd.clear()
	#capping off num at 1000 since we want comfortable room for the display
        if num >= 1000:
            num = 999
            lcd.set_cursor_pos(0,11)
            lcd.print(" MAX ")
	#setting the min
        elif num <= -1000:
            num = -999
            lcd.set_cursor_pos(0,12)
            lcd.print(" MIN")

    #untoggling the button holding variable
    if button_alt.value:
        toggle1 = 0

    #changing the modifier cycling through the mods list
    if not button_ud.value and toggle2 = 0:
        toggle2 = 1
        m += 1
        if m <= 7:
            mod = mods[m]
        else:
            m = 0
            mod = mods[m]
        lcd.clear()

    if button_ud.value:
        toggle2 = 0

    #resetting the modifier and number to 1 and 0
    if not button_res.value:
        lcd.clear()
        lcd.print("  Resetting...")
        num = 0
        m = 0
        mod = mods[m]
        time.sleep(.5)
        lcd.clear()