import board
import busio
import time
import digitalio
import sh1106
from kmk.bootcfg import bootcfg
from digitalio import Direction
from adafruit_mcp230xx.mcp23008 import MCP23008
from adafruit_mcp230xx.mcp23017 import MCP23017
from adafruit_debouncer import Debouncer
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.scanners import DiodeOrientation


i2c = busio.I2C(board.SCL, board.SDA)
display = sh1106.SH1106_I2C(128, 64, i2c, addr=0x3C)
keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

display.fill(0)                          
display.text("hai omelette", 0, 30, 1)   
display.show()                           

def send_key(keyboard, key):
    keyboard.keys_pressed.add(key)
    keyboard.hid_pending = True
    #iirc itll wait
    keyboard.keys_pressed.discard(key)
    keyboard.hid_pending = True






try:
    knob = MCP23008(i2c, address=0x25)
except (OSError, ValueError):
    knob = None
pinA = knob.get_pin(4)
pinA.direction = digitalio.Direction.INPUT
pinA.pull = digitalio.Pull.UP

pinB = knob.get_pin(0)
pinB.direction = digitalio.Direction.INPUT
pinB.pull = digitalio.Pull.UP

pinSW = knob.get_pin(2)
pinSW.direction = digitalio.Direction.INPUT
pinSW.pull = digitalio.Pull.UP
switch = Debouncer(pinSW)

transitions = {
    (0,0,0,1): 1, 
    (0,0,1,0): -1,
    (0,1,1,1): 1, 
    (0,1,0,0): -1,
    (1,1,1,0): 1, 
    (1,1,0,1): -1,
    (1,0,0,1): 1, 
    (1,0,1,1): -1,
}

old_state = (pinA.value,pinB.value)

mps = []
mpswitches = []
try:
    mp = MCP23008(i2c, address=0x25)
    
    
except (OSError, ValueError):
    mp = None

if not mp is None:
    for i in range(4):
        mps.append[mp.get_pin(i)]  
        
        mps[i].direction = digitalio.Direction.INPUT
        mps[i].pull = digitalio.Pull.UP
        mpswitches.append[Debouncer(mps[i])]

    

try:
    
    numkey = KMKKeyboard()
    numpad = MCP23017(i2c, address=0x23)
    
    numkey.keymap = [
    [
        KC.NUM_LOCK, KC.KP_SLASH,    KC.KP_ASTERISK, KC.KP_MINUS,
        KC.KP_7,     KC.KP_8,        KC.KP_9,        KC.KP_PLUS,
        KC.KP_4,     KC.KP_5,        KC.KP_6,        KC.NO,       
        KC.KP_1,     KC.KP_2,        KC.KP_3,        KC.KP_ENTER,
        KC.KP_0,     KC.NO,          KC.KP_DOT,      KC.NO,       
    ]
    
    numkey.row_pins = (knob.get_pin(11),knob.get_pin(10),knob.get_pin(9),knob.get_pin(8),knob.get_pin(7))
    numkey.row_pins = (knob.get_pin(6),knob.get_pin(5),knob.get_pin(4),knob.get_pin(3))
    numkey.diode_orientation = DiodeOrientation.COLUMNS
]
except (OSError, ValueError):
    numpad = None



while True:
    
    if not knob is None:
        new_state = (pinA.value,pinB.value)
        if not new_state == old_state:
            leKey = transitions.get(old_state+new_state,0)
            if leKey == -1:
                send_key(keyboard, KC.VOLD)
            if leKey == 1:
                send_key(keyboard, KC.VOLU)
            
            switch.update()
            if switch.fell:
                send_key(keyboard, KC.MUTE)
            old_state = new_state
    if not mp is None:
        for i in range(4):
            mpswitches[i].update()
            if mpswitches[i].fell:
                if i == 0:
                    send_key(keyboard,KC.LGUI(KC.A))
                elif i == 1:
                    send_key(keyboard,KC.LGUI(KC.V))
                elif i == 2:
                    send_key(keyboard,KC.LGUI(KC.C))    
                elif i == 3:
                    send_key(keyboard,KC.LGUI(KC.X))    
        
    time.sleep(0.001)
            
            
            
            
            
            
            
            
