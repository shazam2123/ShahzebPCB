import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.modules.macros import Press, Release, Tap, Delay
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display.ssd1306 import SSD1306
import busio


keyboard = KMKKeyboard()
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.row_pins = (board.D8, board.D9, board.D10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
macros = Macros()
KC.MACRO(
    on_press=None, 
    on_hold=None,
    on_release=None,
    blocking=True,
)
keyboard.extensions.append(macros)
OPEN_Youtube = KC.MACRO(
    Press(KC.LGUI),
    Tap(KC.R),
    Release(KC.LGUI),
    Delay(500), 
    Tap(KC.W), 
    Tap(KC.ENTER)
)

Alt_Tab = KC.MACRO(
    Press(KC.LALT),
    Delay(30),
    Tap(KC.TAB),
    Delay(30),
    Release(KC.LALT),
)

keyboard.keymap = [
    [OPEN_Youtube, Alt_Tab, KC.N3, KC.N0,
    KC.N4, KC.N5, KC.N6, KC.NO,
    KC.N7, KC.N8, KC.N9, KC.NO],
]



encoder_handler = EncoderHandler()





encoder_handler.pins = ( (board.D6, board.D7, None, False, 2), ) 
keyboard.modules.append(encoder_handler)

keyboard.extensions.append(MediaKeys())
encoder_handler.map = [ ((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, KC.NO),),]                      


i2c = busio.I2C(board.SCL, board.SDA)

driver = SSD1306(
    i2c=i2c,
    device_address=0x3C,
)


display = Display(
    display=driver,
    entries=[(image="3.bmp"),],

    width=128,
    height=32,
    flip = True, 
    dim_time=15, 
    dim_target=0.1, 
    off_time=30, 


)

keyboard.extensions.append(display)



if __name__ == '__main__':
    keyboard.go()